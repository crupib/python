from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Iterable, Optional
from urllib.parse import urljoin

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ============================================================
# Mantle Edge test configuration
# ============================================================

URL = "https://192.168.133.131:4443"
USERNAME = "admin"
PASSWORD = "75@dm1nPa$$W0rd"

WAIT_SECONDS = 15
TAB_HOLD_SECONDS = 2.0
CLICK_SETTLE_SECONDS = 0.50
SCROLL_STEP_PAUSE = 0.45
TOGGLE_SETTLE_SECONDS = 1.50

# Keep false for normal testing. The suite will open confirmation dialogs for
# destructive controls when practical, but it will not confirm them.
ALLOW_DESTRUCTIVE_ACTIONS = False

SETTINGS_TABS = [
    ("Appliance", "appliance"),
    ("Managed Apps", "managed-apps"),
    ("Assets", "assets"),
    ("Actions", "actions"),
    ("System Actions", "system-actions"),
    ("NICs", "nics"),
]

MAIN_PAGES = [
    "Dashboard",
    "Utilization",
    "Profiles",
    "Logs",
    "Edit NICs",
]

DANGEROUS_TERMS = (
    "shutdown",
    "power off",
    "reboot",
    "restart",
    "delete",
    "remove",
    "uninstall",
    "destroy",
    "factory reset",
    "wipe",
)


# ============================================================
# Browser setup
# ============================================================

options = webdriver.ChromeOptions()
options.set_capability("acceptInsecureCerts", True)
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")

driver: Optional[webdriver.Chrome] = None
wait: Optional[WebDriverWait] = None


# ============================================================
# Small helpers
# ============================================================


def header(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def sleep(seconds: float) -> None:
    time.sleep(seconds)


def app_url(path: str) -> str:
    return urljoin(URL.rstrip("/") + "/", path.lstrip("/"))


def page_ready(timeout: int = WAIT_SECONDS) -> None:
    assert driver is not None
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except TimeoutException:
        print("WARNING: document.readyState did not reach complete in time")


def visible(elements: Iterable[WebElement]) -> list[WebElement]:
    """Return displayed elements while tolerating stale/None WebElements."""
    found: list[WebElement] = []
    for element in elements:
        if element is None:
            continue
        try:
            if element.is_displayed():
                found.append(element)
        except (StaleElementReferenceException, WebDriverException, AttributeError):
            continue
    return found


def scroll_into_view(element: WebElement) -> None:
    assert driver is not None
    try:
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center',inline:'center',behavior:'instant'});",
            element,
        )
    except WebDriverException:
        pass


def raw_click(element: WebElement) -> bool:
    assert driver is not None
    scroll_into_view(element)
    sleep(0.15)
    try:
        element.click()
        return True
    except (ElementClickInterceptedException, ElementNotInteractableException, WebDriverException):
        try:
            driver.execute_script("arguments[0].click();", element)
            return True
        except WebDriverException:
            return False


def find_first(locators: Iterable[tuple[str, str]], timeout: float = 5.0) -> Optional[WebElement]:
    assert driver is not None
    deadline = time.time() + timeout
    while time.time() < deadline:
        for by, value in locators:
            try:
                for element in driver.find_elements(by, value):
                    try:
                        if element.is_displayed() and element.is_enabled():
                            return element
                    except StaleElementReferenceException:
                        continue
            except WebDriverException:
                continue
        sleep(0.1)
    return None


def click_exact_text(text: str, timeout: float = 5.0) -> bool:
    """Click a real visible link/button/tab whose text is exactly text."""
    locators = [
        (By.XPATH, f"//button[normalize-space(.)={xpath_literal(text)}]"),
        (By.XPATH, f"//a[normalize-space(.)={xpath_literal(text)}]"),
        (By.XPATH, f"//*[@role='tab' and normalize-space(.)={xpath_literal(text)}]"),
        (By.XPATH, f"//*[normalize-space(.)={xpath_literal(text)}]"),
    ]
    element = find_first(locators, timeout)
    if element is None:
        return False
    ok = raw_click(element)
    if ok:
        print(f"PASS: clicked element '{text}'")
    return ok


def xpath_literal(value: str) -> str:
    if "'" not in value:
        return f"'{value}'"
    if '"' not in value:
        return f'"{value}"'
    pieces = value.split("'")
    return "concat(" + ", \"'\", ".join(f"'{piece}'" for piece in pieces) + ")"


def text_present(text: str, timeout: float = 5.0) -> bool:
    """Return True when matching text is visible.

    This intentionally avoids Selenium's visibility_of_element_located expected
    condition.  In this application React can briefly detach/recreate the node
    during route changes; some Selenium versions then surface a None value into
    the visibility check and raise AttributeError: NoneType has no is_displayed.
    """
    assert driver is not None
    locator = (By.XPATH, f"//*[contains(normalize-space(.), {xpath_literal(text)})]")
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            elements = driver.find_elements(*locator) or []
        except WebDriverException:
            elements = []
        for element in elements:
            if element is None:
                continue
            try:
                if element.is_displayed():
                    return True
            except (StaleElementReferenceException, WebDriverException, AttributeError):
                continue
        sleep(0.10)
    return False


def print_url() -> None:
    assert driver is not None
    print(f"URL: {driver.current_url}")


def escape_to_close_overlay() -> None:
    assert driver is not None
    try:
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        sleep(0.25)
    except WebDriverException:
        pass


def close_visible_dialog() -> bool:
    assert driver is not None
    locators = [
        (By.CSS_SELECTOR, "button[aria-label='Close']"),
        (By.CSS_SELECTOR, "button[aria-label='Close log preview']"),
        (By.XPATH, "//button[normalize-space(.)='Cancel']"),
        (By.XPATH, "//button[normalize-space(.)='Close']"),
    ]
    element = find_first(locators, 1.0)
    if element is not None and raw_click(element):
        sleep(0.25)
        return True
    escape_to_close_overlay()
    return False


# ============================================================
# Real scrolling
# ============================================================


def _scrollable_elements() -> list[WebElement]:
    """Find actual scroll containers, including the document scroller."""
    assert driver is not None
    script = r"""
        const all = [document.scrollingElement, ...document.querySelectorAll('*')];
        const out = [];
        const seen = new Set();
        for (const el of all) {
            if (!el || seen.has(el)) continue;
            seen.add(el);
            const style = getComputedStyle(el);
            const oy = style.overflowY;
            const scrollable = el.scrollHeight > el.clientHeight + 20 &&
                (el === document.scrollingElement || oy === 'auto' || oy === 'scroll');
            if (!scrollable) continue;
            const r = el.getBoundingClientRect();
            if (el !== document.scrollingElement && (r.width < 100 || r.height < 100)) continue;
            out.push(el);
        }
        return out;
    """
    try:
        return driver.execute_script(script) or []
    except WebDriverException:
        return []


def scroll_current_page(label: str) -> None:
    """Visibly scroll each real scroll container from top to bottom and back."""
    assert driver is not None
    header(f"SCROLLING: {label}")

    containers = _scrollable_elements()
    if not containers:
        print("INFO: no vertically scrollable container detected on this view")
        return

    for index, container in enumerate(containers, start=1):
        try:
            metrics = driver.execute_script(
                "return {top:arguments[0].scrollTop, height:arguments[0].scrollHeight, client:arguments[0].clientHeight};",
                container,
            )
            max_top = max(0, int(metrics["height"] - metrics["client"]))
            if max_top <= 0:
                continue

            driver.execute_script("arguments[0].scrollTop = 0;", container)
            sleep(0.25)
            step = max(250, int(metrics["client"] * 0.70))
            print(f"INFO: scroll container {index}: max={max_top}px step={step}px")

            position = 0
            while position < max_top:
                position = min(max_top, position + step)
                driver.execute_script("arguments[0].scrollTop = arguments[1];", container, position)
                actual = int(
                    driver.execute_script("return arguments[0].scrollTop;", container) or 0
                )
                print(f"  scrollTop={actual}px")
                sleep(SCROLL_STEP_PAUSE)
                if actual >= max_top - 2:
                    break

            sleep(0.5)
            driver.execute_script("arguments[0].scrollTop = 0;", container)
            sleep(0.25)
        except (StaleElementReferenceException, WebDriverException) as exc:
            print(f"WARNING: scroll container {index} could not be completed: {exc}")


# ============================================================
# Gear -> Settings -> Admin login
# ============================================================


def click_gear_settings() -> bool:
    """Open Settings using the real gear control in the left shell."""
    assert driver is not None
    header("OPEN SETTINGS WITH GEAR")

    direct = find_first(
        [
            (By.CSS_SELECTOR, "[aria-label='Settings']"),
            (By.CSS_SELECTOR, "[title='Settings']"),
            (By.CSS_SELECTOR, "a[href*='/settings']"),
            (By.CSS_SELECTOR, "button[aria-label*='setting' i]"),
            (By.CSS_SELECTOR, "button[title*='setting' i]"),
        ],
        3.0,
    )
    if direct is not None and raw_click(direct):
        page_ready(8)
        print("PASS: Settings opened using gear/settings element")
        return True

    # Fallback specifically targets a small clickable control in the lower-left
    # sidebar area. This is only a fallback for builds where the icon has no
    # accessible label.
    width = driver.execute_script("return window.innerWidth") or 1400
    height = driver.execute_script("return window.innerHeight") or 900
    candidates = visible(driver.find_elements(By.XPATH, "//button|//a"))
    positional: list[tuple[float, WebElement]] = []
    for element in candidates:
        try:
            rect = element.rect
            if (
                rect.get("x", width) < width * 0.22
                and rect.get("y", 0) > height * 0.70
                and 12 <= rect.get("width", 0) <= 90
                and 12 <= rect.get("height", 0) <= 90
            ):
                positional.append((rect.get("y", 0), element))
        except WebDriverException:
            pass

    for _, element in sorted(positional, key=lambda item: item[0], reverse=True):
        try:
            html = (element.get_attribute("outerHTML") or "").lower()
            if any(term in html for term in ("gear", "setting", "cog")) or positional:
                if raw_click(element):
                    sleep(0.5)
                    if "/settings" in driver.current_url or text_present("Admin Login", 2):
                        print("PASS: Settings opened using lower-left gear fallback")
                        return True
        except WebDriverException:
            continue

    print("FAIL: Settings gear was not found")
    return False


def login_admin() -> bool:
    """Use the exact IDs from AdminLoginTab.tsx."""
    assert driver is not None
    header("ADMIN LOGIN")

    # Already authenticated: AdminLoginTab renders "Logged in as <user>" and Logout.
    if text_present("Logged in as", 1.0):
        print("PASS: already logged in as admin")
        return True

    username = find_first([(By.ID, "admin-username")], 5.0)
    password = find_first([(By.ID, "admin-password")], 5.0)
    if username is None or password is None:
        print("FAIL: #admin-username or #admin-password was not found")
        return False

    username.clear()
    username.send_keys(USERNAME)
    password.clear()
    password.send_keys(PASSWORD)

    login_button = find_first(
        [
            (By.XPATH, "//button[normalize-space(.)='Login']"),
            (By.CSS_SELECTOR, "button[type='submit']"),
        ],
        3.0,
    )
    if login_button is None or not raw_click(login_button):
        print("FAIL: Admin Login button could not be clicked")
        return False

    try:
        WebDriverWait(driver, WAIT_SECONDS).until(
            lambda d: bool(
                visible(d.find_elements(By.XPATH, "//*[contains(normalize-space(.),'Logged in as')]") )
                or visible(d.find_elements(By.XPATH, "//button[normalize-space(.)='Logout']"))
            )
        )
    except TimeoutException:
        print("FAIL: authenticated Admin Login state was not detected")
        return False

    print("PASS: authenticated admin state detected")
    return True


# ============================================================
# Settings top tabs based on SettingsTabPage.tsx
# ============================================================


@dataclass(frozen=True)
class SettingsSpec:
    name: str
    path: str
    expected_text: tuple[str, ...]


SETTINGS_SPECS = [
    SettingsSpec("Appliance", "appliance", ("System Tools", "Deployment Mode")),
    SettingsSpec("Managed Apps", "managed-apps", ("Add Services", "Current Apps")),
    SettingsSpec("Assets", "assets", ("Assets",)),
    SettingsSpec("Actions", "actions", ("Actions",)),
    SettingsSpec("System Actions", "system-actions", ("System Actions",)),
    SettingsSpec("NICs", "nics", ("NIC Roles",)),
]


def open_settings_tab(spec: SettingsSpec) -> bool:
    """Click the actual top tab; route fallback uses the path from SettingsTabPage.tsx."""
    assert driver is not None
    header(f"SETTINGS TAB: {spec.name}")

    clicked = click_exact_text(spec.name, 3.0)
    if clicked:
        try:
            WebDriverWait(driver, 5).until(
                lambda d: f"/settings/{spec.path}" in d.current_url
            )
        except TimeoutException:
            pass

    if f"/settings/{spec.path}" not in driver.current_url:
        print(f"INFO: tab click did not change route; navigating to /settings/{spec.path}")
        driver.get(app_url(f"/settings/{spec.path}"))
        page_ready(8)

    found_expected = False
    for text in spec.expected_text:
        if text_present(text, 4.0):
            print(f"PASS: found expected element text '{text}'")
            found_expected = True
            break

    print_url()
    print(f"INFO: staying on {spec.name} for {TAB_HOLD_SECONDS:.0f} seconds")
    sleep(TAB_HOLD_SECONDS)
    scroll_current_page(spec.name)
    return found_expected


def test_appliance_controls() -> None:
    """Exercise safe Appliance elements without confirming reboot/shutdown."""
    assert driver is not None
    header("APPLIANCE ELEMENTS")

    for button_text in ("Shutdown", "Restart"):
        button = find_first(
            [(By.XPATH, f"//button[normalize-space(.)={xpath_literal(button_text)}]")],
            1.0,
        )
        if button is None:
            continue
        if raw_click(button):
            sleep(0.4)
            print(f"PASS: opened {button_text} confirmation")
            # Never confirm destructive power operations during a normal UI test.
            cancel = find_first(
                [(By.XPATH, "//button[normalize-space(.)='Cancel']")],
                1.0,
            )
            if cancel is not None:
                raw_click(cancel)
                print(f"PASS: cancelled {button_text} confirmation")
            else:
                escape_to_close_overlay()


def test_managed_apps_controls() -> None:
    assert driver is not None
    header("MANAGED APPS ELEMENTS")
    for label in ("Docker Compose", "Systemd Service"):
        if click_exact_text(label, 1.5):
            sleep(0.4)
            # CreateManagedAppModal has a Cancel button.
            cancel = find_first([(By.XPATH, "//button[normalize-space(.)='Cancel']")], 1.5)
            if cancel is not None:
                raw_click(cancel)
                print(f"PASS: opened and cancelled '{label}' create modal")
            else:
                escape_to_close_overlay()


def test_settings_tabs() -> None:
    for spec in SETTINGS_SPECS:
        open_settings_tab(spec)
        if spec.path == "appliance":
            test_appliance_controls()
        elif spec.path == "managed-apps":
            test_managed_apps_controls()


# ============================================================
# Dashboard using elements from DefaultDashboard.tsx
# ============================================================


def open_dashboard() -> bool:
    """Open /dashboard and verify the Dashboard DOM without fragile EC helpers."""
    assert driver is not None
    header("OPEN DASHBOARD")

    try:
        driver.get(app_url("/dashboard"))
        page_ready(8)
    except WebDriverException as exc:
        print(f"FAIL: could not navigate to Dashboard: {exc}")
        return False

    markers = ("Dashboard", "Services", "Compose Projects")
    found: list[str] = []
    for marker in markers:
        try:
            if text_present(marker, 3.0):
                found.append(marker)
        except (WebDriverException, AttributeError) as exc:
            print(f"WARNING: Dashboard marker check failed for {marker}: {exc}")

    if not found:
        print("FAIL: Dashboard elements were not detected")
        try:
            print_url()
        except WebDriverException:
            pass
        return False

    print(f"PASS: Dashboard detected using: {', '.join(found)}")
    print_url()
    sleep(1.0)
    return True


def read_toggle_state(element: WebElement) -> Optional[bool]:
    assert driver is not None
    try:
        aria_checked = element.get_attribute("aria-checked")
        if aria_checked in ("true", "false"):
            return aria_checked == "true"
    except WebDriverException:
        pass

    try:
        aria_pressed = element.get_attribute("aria-pressed")
        if aria_pressed in ("true", "false"):
            return aria_pressed == "true"
    except WebDriverException:
        pass

    try:
        if element.tag_name.lower() == "input":
            return bool(driver.execute_script("return arguments[0].checked;", element))
    except WebDriverException:
        pass

    return None


def visible_on_off_controls(scope: Optional[WebElement] = None) -> list[WebElement]:
    """Locate visible On/Off controls, preferring the currently open tool menu.

    The earlier test returned the first switch anywhere on the page.  On a
    dashboard with several tiles that can select the wrong tile's control.  The
    new version first anchors on the visible ``On/Off`` label and finds the
    switch/checkable control in the same menu/container.
    """
    assert driver is not None
    root = scope if scope is not None else driver
    controls: list[WebElement] = []
    seen: set[str] = set()

    def add(element: Optional[WebElement]) -> None:
        if element is None:
            return
        try:
            if not element.is_displayed() or not element.is_enabled():
                return
            key = element.id
        except (StaleElementReferenceException, WebDriverException, AttributeError):
            return
        if key not in seen:
            seen.add(key)
            controls.append(element)

    # Best path: exact visible label -> nearest ancestor that contains a switch.
    try:
        labels = root.find_elements(By.XPATH, ".//*[normalize-space(.)='On/Off']" if scope is not None else "//*[normalize-space(.)='On/Off']")
    except WebDriverException:
        labels = []

    for label in visible(labels):
        current: Optional[WebElement] = label
        for _ in range(6):
            if current is None:
                break
            try:
                candidates = current.find_elements(
                    By.XPATH,
                    ".//*[@role='switch' or @role='checkbox' or @aria-checked or @aria-pressed or (self::input and (@type='checkbox' or @type='radio'))]",
                )
                for candidate in visible(candidates):
                    add(candidate)
                if controls:
                    break
                current = current.find_element(By.XPATH, "..")
            except (NoSuchElementException, StaleElementReferenceException, WebDriverException):
                break

    if controls:
        return controls

    # Fallbacks for component-library implementations where the label itself is
    # a button or the switch has no explicit label relationship.
    locators = [
        (By.CSS_SELECTOR, "[role='switch']"),
        (By.CSS_SELECTOR, "[role='checkbox']"),
        (By.CSS_SELECTOR, "input[type='checkbox']"),
        (By.CSS_SELECTOR, "button[aria-checked]"),
        (By.CSS_SELECTOR, "button[aria-pressed]"),
        (By.XPATH, ".//button[contains(normalize-space(.),'On/Off')]" if scope is not None else "//button[contains(normalize-space(.),'On/Off')]"),
    ]
    for by, value in locators:
        try:
            elements = root.find_elements(by, value)
        except WebDriverException:
            continue
        for element in visible(elements):
            add(element)
    return controls

def open_tile_tools(tile: WebElement) -> bool:
    """Use controls inside a Service/Compose tile to reveal its tool actions."""
    assert driver is not None
    # Prefer explicit menu/tool attributes if Tile.tsx provides them.
    selectors = [
        "button[aria-label*='action' i]",
        "button[aria-label*='menu' i]",
        "button[aria-label*='more' i]",
        "button[aria-label*='tool' i]",
        "button[title*='action' i]",
        "button[title*='menu' i]",
        "button[title*='more' i]",
        "button[title*='tool' i]",
        "button",
    ]

    for selector in selectors:
        try:
            buttons = visible(tile.find_elements(By.CSS_SELECTOR, selector))
        except WebDriverException:
            continue
        for button in buttons:
            try:
                text = " ".join((button.text or "").split()).lower()
                aria = (button.get_attribute("aria-label") or "").lower()
                title = (button.get_attribute("title") or "").lower()
                combined = f"{text} {aria} {title}"
                if any(word in combined for word in DANGEROUS_TERMS):
                    continue
                # For the generic button fallback, only use compact/icon buttons.
                if selector == "button":
                    rect = button.rect
                    if rect.get("width", 999) > 90 or rect.get("height", 999) > 90:
                        continue
                if raw_click(button):
                    sleep(0.35)
                    if visible_on_off_controls():
                        return True
            except (StaleElementReferenceException, WebDriverException):
                continue
    return bool(visible_on_off_controls())


def dashboard_tiles() -> list[tuple[str, WebElement]]:
    """Find tile containers from the Service/Compose Project subtitle elements."""
    assert driver is not None
    results: list[tuple[str, WebElement]] = []
    seen: set[str] = set()

    for subtitle in ("Service", "Compose Project"):
        nodes = visible(
            driver.find_elements(
                By.XPATH,
                f"//*[normalize-space(.)={xpath_literal(subtitle)}]",
            )
        )
        for node in nodes:
            # Walk upward until we have a reasonably sized container with buttons.
            container: Optional[WebElement] = None
            current = node
            for _ in range(7):
                try:
                    current = current.find_element(By.XPATH, "..")
                    rect = current.rect
                    buttons = current.find_elements(By.TAG_NAME, "button")
                    if buttons and rect.get("width", 0) >= 180 and rect.get("height", 0) >= 80:
                        container = current
                        break
                except (NoSuchElementException, StaleElementReferenceException, WebDriverException):
                    break

            if container is None:
                continue

            try:
                key = container.id
                title_text = " ".join((container.text or "").split())[:120]
            except WebDriverException:
                continue
            if key in seen:
                continue
            seen.add(key)
            results.append((title_text or subtitle, container))

    return results


def _wait_for_toggle_state_change(previous: Optional[bool], timeout: float = 8.0) -> tuple[Optional[WebElement], Optional[bool]]:
    """Re-find the active On/Off control and wait for a real state change."""
    deadline = time.time() + timeout
    last_control: Optional[WebElement] = None
    last_state: Optional[bool] = None
    while time.time() < deadline:
        controls = visible_on_off_controls()
        for control in controls:
            state = read_toggle_state(control)
            last_control, last_state = control, state
            if previous is None:
                return control, state
            if state is not None and state != previous:
                return control, state
        sleep(0.20)
    return last_control, last_state


def _wait_for_toggle_state(target: Optional[bool], timeout: float = 8.0) -> tuple[Optional[WebElement], Optional[bool]]:
    """Re-find the active On/Off control and wait until it reaches target."""
    deadline = time.time() + timeout
    last_control: Optional[WebElement] = None
    last_state: Optional[bool] = None
    while time.time() < deadline:
        controls = visible_on_off_controls()
        for control in controls:
            state = read_toggle_state(control)
            last_control, last_state = control, state
            if target is None or state == target:
                return control, state
        sleep(0.20)
    return last_control, last_state


def toggle_control_twice(control: WebElement, description: str) -> bool:
    """Exercise both states and restore the starting state.

    A PASS is reported only if the first click changes state and the second
    click restores the original state.  This fixes the old false PASS such as
    ``False -> False -> False`` seen on the compose-project tile.
    """
    before = read_toggle_state(control)
    print(f"INFO: {description} toggle start state = {before}")

    if before is None:
        print(f"WARNING: could not determine starting toggle state for {description}")
        return False

    if not raw_click(control):
        print(f"WARNING: first toggle click failed for {description}")
        return False

    control2, middle = _wait_for_toggle_state_change(before, timeout=max(TOGGLE_SETTLE_SECONDS, 8.0))
    if control2 is None or middle is None or middle == before:
        print(f"FAIL: {description} did not change state after first click: {before} -> {middle}")
        return False
    print(f"PASS: {description} toggle changed to {middle}")

    if not raw_click(control2):
        print(f"WARNING: second toggle click failed for {description}")
        return False

    _control3, after = _wait_for_toggle_state(before, timeout=max(TOGGLE_SETTLE_SECONDS, 8.0))
    if after != before:
        print(f"FAIL: {description} was not restored: {before} -> {middle} -> {after}")
        return False

    print(f"PASS: {description} toggled twice/restored: {before} -> {middle} -> {after}")
    return True

def test_dashboard_tiles() -> None:
    assert driver is not None
    header("DASHBOARD SERVICE / COMPOSE TILE ELEMENTS")

    tiles = dashboard_tiles()
    print(f"INFO: discovered {len(tiles)} Service/Compose tile container(s)")

    for index, (description, tile) in enumerate(tiles, start=1):
        print(f"\n--- TILE {index}: {description} ---")
        try:
            scroll_into_view(tile)
            sleep(0.35)
            if not open_tile_tools(tile):
                print("WARNING: could not reveal an On/Off control for this tile")
                continue

            controls = visible_on_off_controls()
            if not controls:
                print("WARNING: no visible On/Off control after opening tile tools")
                continue

            toggle_control_twice(controls[0], description)
            escape_to_close_overlay()
        except (StaleElementReferenceException, WebDriverException) as exc:
            print(f"WARNING: tile test failed: {exc}")


def test_dashboard_controls() -> None:
    assert driver is not None
    header("DASHBOARD NAMED ELEMENTS")

    # These titles are defined in DefaultDashboard.tsx.
    for title in ("Change Profile", "Dashboard Help", "Select Profile"):
        element = find_first([(By.CSS_SELECTOR, f"[title={xpath_literal(title)}]")], 0.5)
        # CSS cannot use XPath literals. Fallback to XPath immediately.
        if element is None:
            element = find_first([(By.XPATH, f"//*[@title={xpath_literal(title)}]")], 0.5)
        if element is None:
            continue
        if raw_click(element):
            print(f"PASS: clicked Dashboard control '{title}'")
            sleep(0.4)
            close_visible_dialog()

    # SystemActionsModal.tsx renders a System Actions heading and Close button.
    execute = find_first(
        [
            (By.XPATH, "//button[contains(normalize-space(.),'Execute System Action')]"),
            (By.XPATH, "//*[contains(normalize-space(.),'Execute System Action')]/ancestor::button[1]"),
        ],
        1.5,
    )
    if execute is not None and raw_click(execute):
        print("PASS: opened Execute System Action modal")
        sleep(0.5)
        text_present("System Actions", 1.0)
        close_visible_dialog()


# ============================================================
# Other shell pages using page source element text
# ============================================================


def click_sidebar_page(name: str) -> bool:
    assert driver is not None
    header(f"MAIN PAGE: {name}")
    if click_exact_text(name, 2.5):
        page_ready(8)
        sleep(0.7)
        print_url()
        return True
    print(f"WARNING: sidebar element '{name}' was not found")
    return False


def test_utilization() -> None:
    if not click_sidebar_page("Utilization"):
        return
    if text_present("System Metrics", 4):
        print("PASS: System Metrics found")
    scroll_current_page("Utilization")


def test_profiles() -> None:
    if not click_sidebar_page("Profiles"):
        return
    if text_present("Profiles", 4):
        print("PASS: Profiles heading found")
    scroll_current_page("Profiles")


def test_logs() -> None:
    if not click_sidebar_page("Logs"):
        return
    if text_present("Action Logs", 4):
        print("PASS: Action Logs element found")
    scroll_current_page("Logs")


def test_edit_nics() -> None:
    if not click_sidebar_page("Edit NICs"):
        return
    if text_present("Edit NIC Assignments", 4):
        print("PASS: Edit NIC Assignments heading found")
    scroll_current_page("Edit NICs")


# ============================================================
# Main
# ============================================================


def main() -> None:
    global driver, wait

    header("STARTING MANTLE EDGE ELEMENT-DRIVEN SELENIUM TEST")
    print("INFO: selectors and expected text are based on the supplied TSX page elements")

    try:
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(
            driver,
            WAIT_SECONDS,
            poll_frequency=0.25,
            ignored_exceptions=(StaleElementReferenceException, NoSuchElementException),
        )
        print("PASS: Chrome started")

        # ----------------------------------------------------
        # 1. Open normal shell/dashboard.
        # ----------------------------------------------------
        driver.get(URL)
        page_ready()
        print("PASS: Mantle Edge opened")
        print_url()

        # ----------------------------------------------------
        # 2. Gear -> Settings -> Admin Login using exact IDs.
        # ----------------------------------------------------
        if not click_gear_settings():
            raise RuntimeError("Unable to open Settings with the gear control")

        # SettingsTabPage defaults to Admin Login for non-authenticated users.
        if "/settings" in driver.current_url and "admin-login" not in driver.current_url:
            # Clicking Admin Login is preferred; route fallback is deterministic.
            if not click_exact_text("Admin Login", 2.0):
                driver.get(app_url("/settings/admin-login"))
                page_ready(8)

        if not login_admin():
            raise RuntimeError("Admin login was not confirmed")

        # ----------------------------------------------------
        # 3. EXACT top menu traversal from SettingsTabPage.tsx.
        #    Every tab is displayed for two seconds, then scrolled.
        # ----------------------------------------------------
        test_settings_tabs()

        # ----------------------------------------------------
        # 4. Explicitly switch to Dashboard DOM and use Dashboard elements.
        # ----------------------------------------------------
        if not open_dashboard():
            raise RuntimeError("Dashboard could not be verified after Settings tests")

        test_dashboard_controls()
        test_dashboard_tiles()
        scroll_current_page("Dashboard")

        # ----------------------------------------------------
        # 5. Remaining left-side pages.
        # ----------------------------------------------------
        test_utilization()
        test_profiles()
        test_logs()
        test_edit_nics()

        # ----------------------------------------------------
        # 6. Predictable final state.
        # ----------------------------------------------------
        if open_dashboard():
            header("TEST COMPLETE")
            print("PASS: element-driven Mantle Edge UI test completed")
        else:
            header("TEST COMPLETE WITH WARNING")
            print("WARNING: all page tests ran, but final Dashboard verification failed")

    except Exception as exc:
        header("TEST FAILED")
        print(f"{type(exc).__name__}: {exc}")
        if driver is not None:
            try:
                print_url()
            except Exception:
                pass

    finally:
        if driver is not None:
            sleep(1.0)
            try:
                driver.quit()
                print("PASS: Chrome closed")
            except WebDriverException as exc:
                print(f"WARNING: Chrome did not close normally: {exc}")


if __name__ == "__main__":
    main()
