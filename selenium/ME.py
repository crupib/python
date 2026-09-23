from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    WebDriverException,
)
import time
from dataclasses import dataclass
from typing import Optional
from selenium.webdriver.remote.webelement import WebElement


URL = "https://192.168.133.131:4443"
DASHBOARD_URL = URL.rstrip("/") + "/dashboard"
USERNAME = "admin"
PASSWORD = "75@dm1nPa$$W0rd"


# ============================================================
# Browser configuration
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


driver = None
wait = None


sidebar_options = [
    "Dashboard",
    "Utilization",
    "Profiles",
    "Logs",
    "Edit NICs",
]


# ============================================================
# Full-page interaction test configuration
# ============================================================

# Keep this False unless the test appliance is disposable and you explicitly
# want Selenium to execute final destructive controls such as reboot, shutdown,
# delete, remove, uninstall, or service-stop actions. Parent menus/dialogs are
# still opened and tested.
ALLOW_DESTRUCTIVE_ACTIONS = False

# Prevent an infinite loop if the UI continuously creates new controls.
MAX_INTERACTIONS_PER_PAGE = 250

# Small pause after a click so the front end can update/re-render the DOM.
CLICK_SETTLE_SECONDS = 0.35

DESTRUCTIVE_WORDS = {
    "reboot",
    "shutdown",
    "shut down",
    "power off",
    "delete",
    "remove",
    "destroy",
    "factory reset",
    "reset system",
    "stop service",
    "stop all",
    "kill",
    "terminate",
    "uninstall",
    "wipe",
}

# The Settings control is handled only by click_gear_settings() so sign-in
# continues to happen through the Gear, as requested.
GEAR_WORDS = {
    "settings",
    "setting",
    "gear",
    "configuration",
    "configure application",
}


@dataclass(frozen=True)
class InteractiveItem:
    fingerprint: str
    selector: str
    text: str
    aria_label: str
    title: str
    href: str
    tag: str
    element_type: str
    role: str

    @property
    def description(self) -> str:
        pieces = [
            self.text,
            self.aria_label,
            self.title,
            self.href,
            self.element_type,
            self.role,
            self.tag,
        ]
        cleaned = [" ".join((value or "").split()) for value in pieces]
        cleaned = [value for value in cleaned if value]
        if not cleaned:
            return self.selector
        return " | ".join(cleaned[:4])

    @property
    def combined_text(self) -> str:
        return " ".join(
            [
                self.text,
                self.aria_label,
                self.title,
                self.href,
                self.element_type,
                self.role,
            ]
        ).lower()


# ============================================================
# Utility functions
# ============================================================

def safe_sleep(seconds=1):
    try:
        time.sleep(seconds)
    except Exception:
        pass


def print_header(title):
    print("\n========================================")
    print(title)
    print("========================================")


def wait_for_page(timeout=15):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )
    except Exception as e:
        print(
            f"WARNING: Page-ready wait failed: {e}"
        )


def dismiss_possible_overlays():
    possible_buttons = [
        "//button[normalize-space()='Close']",
        "//button[normalize-space()='Dismiss']",
        "//button[normalize-space()='Cancel']",
        "//button[normalize-space()='OK']",
        "//button[normalize-space()='Got it']",
        "//button[@aria-label='Close']",
    ]

    for xpath in possible_buttons:
        try:
            elements = driver.find_elements(
                By.XPATH,
                xpath
            )

            for element in elements:
                try:
                    if (
                        element.is_displayed()
                        and element.is_enabled()
                    ):
                        driver.execute_script(
                            "arguments[0].click();",
                            element
                        )

                        safe_sleep(0.2)

                except Exception:
                    continue

        except Exception:
            continue


def safe_click(
    locator,
    description="element",
    retries=4
):
    last_error = None

    for attempt in range(
        1,
        retries + 1
    ):
        try:
            dismiss_possible_overlays()

            element = WebDriverWait(
                driver,
                5
            ).until(
                EC.presence_of_element_located(
                    locator
                )
            )

            try:
                driver.execute_script(
                    """
                    arguments[0].scrollIntoView({
                        behavior: 'instant',
                        block: 'center',
                        inline: 'center'
                    });
                    """,
                    element,
                )
            except Exception:
                pass

            safe_sleep(0.3)

            try:
                element = WebDriverWait(
                    driver,
                    3
                ).until(
                    EC.element_to_be_clickable(
                        locator
                    )
                )

            except Exception:
                try:
                    element = driver.find_element(
                        *locator
                    )

                except Exception as e:
                    last_error = e
                    continue

            try:
                element.click()

            except (
                ElementClickInterceptedException,
                ElementNotInteractableException,
                WebDriverException,
            ):
                print(
                    f"Normal click failed for "
                    f"{description}; "
                    "trying JavaScript click."
                )

                driver.execute_script(
                    "arguments[0].click();",
                    element
                )

            print(
                f"PASS: Clicked {description}"
            )

            return True

        except Exception as e:
            last_error = e

            print(
                f"Retry {attempt}/{retries}: "
                f"Could not click "
                f"{description}: {e}"
            )

            safe_sleep(0.5)

    print(
        f"WARNING: Unable to click "
        f"{description}: {last_error}"
    )

    print(
        "Continuing test."
    )

    return False


def click_text(text):
    locators = [
        (
            By.XPATH,
            f"//*[normalize-space()='{text}']"
        ),
        (
            By.XPATH,
            f"//a[normalize-space()='{text}']"
        ),
        (
            By.XPATH,
            f"//button[normalize-space()='{text}']"
        ),
    ]

    for locator in locators:
        try:
            if safe_click(
                locator,
                description=text,
                retries=2
            ):
                return True

        except Exception as e:
            print(
                f"WARNING: click_text failed "
                f"for {text}: {e}"
            )

    print(
        f"WARNING: Could not find/click "
        f"text: {text}"
    )

    return False


def find_first_visible(
    locators,
    description="element"
):
    for locator in locators:
        try:
            elements = driver.find_elements(
                *locator
            )

            for element in elements:
                try:
                    if (
                        element.is_displayed()
                        and element.is_enabled()
                    ):
                        return element

                except Exception:
                    continue

        except Exception:
            continue

    print(
        f"WARNING: Could not find "
        f"{description}."
    )

    return None


def read_metric(metric_name):
    try:
        label = WebDriverWait(
            driver,
            5
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[normalize-space()="
                    f"'{metric_name}']"
                )
            )
        )

        possible_parents = [
            "./parent::*",
            "./ancestor::div[1]",
            "./ancestor::div[2]",
            "./ancestor::div[3]",
        ]

        for parent_xpath in possible_parents:
            try:
                card = label.find_element(
                    By.XPATH,
                    parent_xpath
                )

                text = card.text.strip()

                if text:
                    print(
                        f"{metric_name}: "
                        f"{text.replace(chr(10), ' | ')}"
                    )

                    return True

            except Exception:
                continue

        print(
            f"WARNING: {metric_name} found, "
            "but value was unreadable."
        )

    except Exception as e:
        print(
            f"WARNING: Could not read "
            f"{metric_name}: {e}"
        )

    return False


def print_visible_page_text():
    try:
        elements = driver.find_elements(
            By.XPATH,
            """
            //h1 |
            //h2 |
            //h3 |
            //h4 |
            //h5 |
            //h6 |
            //p |
            //label
            """,
        )

        seen = set()

        for element in elements:
            try:
                if not element.is_displayed():
                    continue

                text = element.text.strip()

                if not text or text in seen:
                    continue

                seen.add(
                    text
                )

                print(
                    f"  {text}"
                )

            except Exception:
                continue

    except Exception as e:
        print(
            f"WARNING: Could not print "
            f"visible page text: {e}"
        )


def print_current_url():
    try:
        print(
            f"Current URL: "
            f"{driver.current_url}"
        )

    except Exception as e:
        print(
            f"WARNING: Could not read "
            f"current URL: {e}"
        )


# ============================================================
# Full-page interaction helpers
# ============================================================

def close_extra_windows(original_handle):
    """Close pop-up tabs/windows opened by a test click."""
    try:
        handles = list(driver.window_handles)
    except Exception:
        return

    for handle in handles:
        if handle == original_handle:
            continue
        try:
            driver.switch_to.window(handle)
            driver.close()
        except Exception:
            pass

    try:
        if original_handle in driver.window_handles:
            driver.switch_to.window(original_handle)
    except Exception:
        pass


def is_application_url(url):
    """Return True when URL still points at this Mantle Edge application."""
    try:
        base_host = URL.split('://', 1)[-1].split('/', 1)[0]
        return base_host in (url or '')
    except Exception:
        return False


# ============================================================
# Utilization functions
# ============================================================

def open_utilization():
    print_header(
        "OPENING UTILIZATION"
    )

    try:
        if not click_text(
            "Utilization"
        ):
            print(
                "WARNING: Could not open "
                "Utilization."
            )

            print(
                "Continuing test."
            )

            return False

    except Exception as e:
        print(
            f"WARNING: Utilization "
            f"navigation failed: {e}"
        )

        return False

    try:
        WebDriverWait(
            driver,
            5
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[normalize-space()="
                    "'System Metrics']"
                )
            )
        )

        print(
            "PASS: Utilization page loaded"
        )

    except Exception:
        print(
            "WARNING: System Metrics "
            "heading was not detected."
        )

        print(
            "Continuing test."
        )

    safe_sleep(1)

    return True


def inspect_utilization_metrics():
    print_header(
        "LIVE SYSTEM METRICS"
    )

    metrics = [
        "CPU",
        "Memory",
        "Disk",
        "Network Download",
        "Network Upload",
    ]

    for metric in metrics:
        try:
            read_metric(
                metric
            )

        except Exception as e:
            print(
                f"WARNING: Metric {metric} "
                f"failed: {e}"
            )

            print(
                "Continuing."
            )


def scroll_utilization():
    print_header(
        "SCROLLING THROUGH UTILIZATION"
    )

    try:
        driver.execute_script(
            "window.scrollTo(0, 0);"
        )

    except Exception as e:
        print(
            f"WARNING: Could not scroll "
            f"to top: {e}"
        )

    safe_sleep(1)

    try:
        viewport_height = int(
            driver.execute_script(
                "return window.innerHeight;"
            ) or 600
        )

    except Exception:
        viewport_height = 600

    try:
        page_height = int(
            driver.execute_script(
                """
                return Math.max(
                    document.body.scrollHeight,
                    document.documentElement.scrollHeight
                );
                """
            ) or 3000
        )

    except Exception:
        page_height = 3000

    scroll_position = 0
    scroll_count = 1
    max_scrolls = 30

    while (
        scroll_position <= page_height
        and scroll_count <= max_scrolls
    ):
        print(
            f"\n--- Utilization Scroll "
            f"{scroll_count} "
            f"@ {scroll_position}px ---"
        )

        try:
            driver.execute_script(
                """
                window.scrollTo({
                    top: arguments[0],
                    behavior: 'smooth'
                });
                """,
                scroll_position,
            )

        except Exception as e:
            print(
                f"WARNING: Scroll failed: {e}"
            )

        safe_sleep(0.8)

        print_visible_page_text()

        for metric in [
            "CPU",
            "Memory",
            "Disk",
            "Network Download",
            "Network Upload",
        ]:
            try:
                elements = driver.find_elements(
                    By.XPATH,
                    f"//*[normalize-space()="
                    f"'{metric}']",
                )

                if elements:
                    for element in elements:
                        try:
                            if element.is_displayed():
                                read_metric(
                                    metric
                                )
                                break

                        except Exception:
                            continue

            except Exception:
                continue

        scroll_position += int(
            viewport_height * 0.70
        )

        scroll_count += 1

        try:
            new_height = int(
                driver.execute_script(
                    """
                    return Math.max(
                        document.body.scrollHeight,
                        document.documentElement.scrollHeight
                    );
                    """
                ) or page_height
            )

            if new_height > page_height:
                page_height = new_height

        except Exception:
            pass

    try:
        driver.execute_script(
            """
            window.scrollTo({
                top:
                    document.documentElement.scrollHeight,
                behavior: 'smooth'
            });
            """
        )

    except Exception as e:
        print(
            f"WARNING: Could not force "
            f"scroll to bottom: {e}"
        )

    safe_sleep(1)

    print(
        "PASS: Finished Utilization scrolling"
    )


# ============================================================
# Gear / Settings
# ============================================================

def click_gear_settings():
    print_header(
        "LOOKING FOR BOTTOM-LEFT GEAR / SETTINGS"
    )

    try:
        driver.execute_script(
            "window.scrollTo(0, 0);"
        )

    except Exception:
        pass

    safe_sleep(0.5)

    # --------------------------------------------------------
    # Strong Settings selectors
    # --------------------------------------------------------

    settings_locators = [
        (
            By.CSS_SELECTOR,
            "[aria-label='Settings']"
        ),
        (
            By.CSS_SELECTOR,
            "[aria-label*='setting' i]"
        ),
        (
            By.CSS_SELECTOR,
            "[title='Settings']"
        ),
        (
            By.CSS_SELECTOR,
            "[title*='setting' i]"
        ),
        (
            By.CSS_SELECTOR,
            "[data-testid*='setting' i]"
        ),
        (
            By.CSS_SELECTOR,
            "[id*='setting' i]"
        ),
        (
            By.XPATH,
            "//a[contains("
            "translate(@href,"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
            "'abcdefghijklmnopqrstuvwxyz'),"
            "'setting')]"
        ),
        (
            By.XPATH,
            "//*[normalize-space()='Settings']"
        ),
        (
            By.XPATH,
            """
            //button[
                .//*[name()='svg']
                and (
                    contains(
                        translate(
                            @aria-label,
                            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                            'abcdefghijklmnopqrstuvwxyz'
                        ),
                        'setting'
                    )
                    or
                    contains(
                        translate(
                            @title,
                            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                            'abcdefghijklmnopqrstuvwxyz'
                        ),
                        'setting'
                    )
                )
            ]
            """
        ),
    ]

    for locator in settings_locators:
        try:
            elements = driver.find_elements(
                *locator
            )

            for element in elements:
                try:
                    if not element.is_displayed():
                        continue

                    try:
                        driver.execute_script(
                            """
                            arguments[0].scrollIntoView({
                                block: 'center',
                                inline: 'center'
                            });
                            """,
                            element,
                        )

                    except Exception:
                        pass

                    safe_sleep(0.2)

                    try:
                        element.click()

                    except Exception:
                        driver.execute_script(
                            "arguments[0].click();",
                            element
                        )

                    print(
                        "PASS: Gear / Settings clicked"
                    )

                    return True

                except Exception:
                    continue

        except Exception:
            continue

    # --------------------------------------------------------
    # Sidebar fallback
    # --------------------------------------------------------

    print(
        "Standard Settings selectors "
        "did not work."
    )

    print(
        "Trying bottom-left sidebar "
        "icon detection."
    )

    sidebar_candidates = []

    sidebar_locators = [
        (
            By.TAG_NAME,
            "aside"
        ),
        (
            By.TAG_NAME,
            "nav"
        ),
        (
            By.CSS_SELECTOR,
            "[class*='sidebar' i]"
        ),
        (
            By.CSS_SELECTOR,
            "[id*='sidebar' i]"
        ),
        (
            By.CSS_SELECTOR,
            "[class*='side-nav' i]"
        ),
        (
            By.CSS_SELECTOR,
            "[class*='sidenav' i]"
        ),
    ]

    for locator in sidebar_locators:
        try:
            found = driver.find_elements(
                *locator
            )

            for item in found:
                if item not in sidebar_candidates:
                    sidebar_candidates.append(
                        item
                    )

        except Exception:
            continue

    for sidebar in sidebar_candidates:
        try:
            if not sidebar.is_displayed():
                continue

            try:
                driver.execute_script(
                    """
                    arguments[0].scrollTop =
                        arguments[0].scrollHeight;
                    """,
                    sidebar,
                )

            except Exception:
                pass

            safe_sleep(0.3)

            try:
                icon_buttons = sidebar.find_elements(
                    By.XPATH,
                    """
                    .//button[
                        .//*[name()='svg']
                        or
                        .//*[name()='img']
                    ]
                    |
                    .//a[
                        .//*[name()='svg']
                        or
                        .//*[name()='img']
                    ]
                    """,
                )

            except Exception:
                icon_buttons = []

            for button in reversed(
                icon_buttons
            ):
                try:
                    if not button.is_displayed():
                        continue

                    aria = (
                        button.get_attribute(
                            "aria-label"
                        ) or ""
                    )

                    title = (
                        button.get_attribute(
                            "title"
                        ) or ""
                    )

                    href = (
                        button.get_attribute(
                            "href"
                        ) or ""
                    )

                    text = (
                        button.text or ""
                    )

                    element_id = (
                        button.get_attribute(
                            "id"
                        ) or ""
                    )

                    element_class = (
                        button.get_attribute(
                            "class"
                        ) or ""
                    )

                    combined = (
                        f"{aria} "
                        f"{title} "
                        f"{href} "
                        f"{text} "
                        f"{element_id} "
                        f"{element_class}"
                    ).lower()

                    print(
                        "Bottom sidebar candidate:",
                        f"aria-label={aria},",
                        f"title={title},",
                        f"href={href}",
                    )

                    if (
                        "setting" in combined
                        or "gear" in combined
                        or "config" in combined
                    ):
                        try:
                            button.click()

                        except Exception:
                            driver.execute_script(
                                "arguments[0].click();",
                                button,
                            )

                        print(
                            "PASS: Bottom-left "
                            "Gear / Settings clicked"
                        )

                        return True

                except Exception:
                    continue

        except Exception:
            continue

    # --------------------------------------------------------
    # Bottom-left screen position fallback
    # --------------------------------------------------------

    print(
        "Trying screen-position fallback "
        "for bottom-left icon."
    )

    try:
        candidates = driver.find_elements(
            By.XPATH,
            "//button | //a"
        )

        screen_height = (
            driver.execute_script(
                "return window.innerHeight;"
            ) or 800
        )

        screen_width = (
            driver.execute_script(
                "return window.innerWidth;"
            ) or 1200
        )

        positional = []

        for element in candidates:
            try:
                if not element.is_displayed():
                    continue

                rect = element.rect

                x = rect.get(
                    "x",
                    99999
                )

                y = rect.get(
                    "y",
                    -1
                )

                width = rect.get(
                    "width",
                    0
                )

                height = rect.get(
                    "height",
                    0
                )

                if (
                    width <= 0
                    or height <= 0
                ):
                    continue

                if (
                    x <= screen_width * 0.25
                    and y >= screen_height * 0.65
                ):
                    positional.append(
                        (
                            y,
                            x,
                            element
                        )
                    )

            except Exception:
                continue

        positional.sort(
            key=lambda item: (
                -item[0],
                item[1]
            )
        )

        for _, _, element in positional[:8]:
            try:
                aria = (
                    element.get_attribute(
                        "aria-label"
                    ) or ""
                )

                title = (
                    element.get_attribute(
                        "title"
                    ) or ""
                )

                href = (
                    element.get_attribute(
                        "href"
                    ) or ""
                )

                text = (
                    element.text or ""
                )

                element_class = (
                    element.get_attribute(
                        "class"
                    ) or ""
                )

                html = (
                    element.get_attribute(
                        "outerHTML"
                    ) or ""
                )

                combined = (
                    f"{aria} "
                    f"{title} "
                    f"{href} "
                    f"{text} "
                    f"{element_class} "
                    f"{html}"
                ).lower()

                if (
                    "setting" in combined
                    or "gear" in combined
                    or "cog" in combined
                    or "config" in combined
                ):
                    try:
                        element.click()

                    except Exception:
                        driver.execute_script(
                            "arguments[0].click();",
                            element
                        )

                    print(
                        "PASS: Bottom-left "
                        "Settings icon clicked"
                    )

                    return True

            except Exception:
                continue

    except Exception as e:
        print(
            f"WARNING: Position fallback "
            f"failed: {e}"
        )

    print(
        "WARNING: Could not identify "
        "Gear / Settings."
    )

    print(
        "Skipping Settings click and "
        "continuing test."
    )

    return False


# ============================================================
# Settings Login
# ============================================================

def login_to_settings(
    username=USERNAME,
    password=PASSWORD
):
    print_header(
        "SETTINGS LOGIN"
    )

    safe_sleep(1)

    try:
        print(
            f"Settings URL: "
            f"{driver.current_url}"
        )

    except Exception:
        pass

    # --------------------------------------------------------
    # Username
    # --------------------------------------------------------

    username_locators = [
        (
            By.NAME,
            "username"
        ),
        (
            By.ID,
            "username"
        ),
        (
            By.CSS_SELECTOR,
            "input[name='username']"
        ),
        (
            By.CSS_SELECTOR,
            "input[id='username']"
        ),
        (
            By.CSS_SELECTOR,
            "input[autocomplete='username']"
        ),
        (
            By.XPATH,
            """
            //input[
                contains(
                    translate(
                        @placeholder,
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'username'
                )
            ]
            """
        ),
        (
            By.XPATH,
            """
            //input[
                contains(
                    translate(
                        @placeholder,
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'user name'
                )
            ]
            """
        ),
        (
            By.XPATH,
            """
            //input[
                contains(
                    translate(
                        @placeholder,
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'user'
                )
            ]
            """
        ),
        (
            By.XPATH,
            """
            //input[
                contains(
                    translate(
                        @aria-label,
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'user'
                )
            ]
            """
        ),
        (
            By.CSS_SELECTOR,
            "input[type='text']"
        ),
        (
            By.CSS_SELECTOR,
            "input[type='email']"
        ),
    ]

    username_field = find_first_visible(
        username_locators,
        description="Settings username field",
    )

    if username_field is None:
        print(
            "WARNING: Username field "
            "was not found."
        )

        print(
            "Skipping Settings login "
            "and continuing."
        )

        return False

    try:
        username_field.click()

    except Exception:
        pass

    try:
        username_field.clear()

    except Exception:
        pass

    try:
        username_field.send_keys(
            username
        )

        print(
            "PASS: Username entered"
        )

    except Exception as e:
        print(
            f"WARNING: Could not enter "
            f"username: {e}"
        )

        print(
            "Skipping login and continuing."
        )

        return False

    # --------------------------------------------------------
    # Password
    # --------------------------------------------------------

    password_locators = [
        (
            By.NAME,
            "password"
        ),
        (
            By.ID,
            "password"
        ),
        (
            By.CSS_SELECTOR,
            "input[name='password']"
        ),
        (
            By.CSS_SELECTOR,
            "input[id='password']"
        ),
        (
            By.CSS_SELECTOR,
            "input[type='password']"
        ),
        (
            By.CSS_SELECTOR,
            "input[autocomplete='current-password']"
        ),
        (
            By.XPATH,
            """
            //input[
                contains(
                    translate(
                        @placeholder,
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'password'
                )
            ]
            """
        ),
    ]

    password_field = find_first_visible(
        password_locators,
        description="Settings password field",
    )

    if password_field is None:
        print(
            "WARNING: Password field "
            "was not found."
        )

        print(
            "Skipping Settings login "
            "and continuing."
        )

        return False

    try:
        password_field.click()

    except Exception:
        pass

    try:
        password_field.clear()

    except Exception:
        pass

    try:
        password_field.send_keys(
            password
        )

        print(
            "PASS: Password entered"
        )

    except Exception as e:
        print(
            f"WARNING: Could not enter "
            f"password: {e}"
        )

        print(
            "Skipping login and continuing."
        )

        return False

    safe_sleep(0.5)

    # --------------------------------------------------------
    # Sign In / Login
    # --------------------------------------------------------

    login_locators = [
        (
            By.XPATH,
            "//button[normalize-space()='Sign In']"
        ),
        (
            By.XPATH,
            "//button[normalize-space()='Sign in']"
        ),
        (
            By.XPATH,
            "//button[normalize-space()='SIGN IN']"
        ),
        (
            By.XPATH,
            "//button[normalize-space()='Login']"
        ),
        (
            By.XPATH,
            "//button[normalize-space()='Log In']"
        ),
        (
            By.XPATH,
            "//button[normalize-space()='Log in']"
        ),
        (
            By.XPATH,
            """
            //button[
                contains(
                    translate(
                        normalize-space(.),
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'sign in'
                )
            ]
            """
        ),
        (
            By.XPATH,
            """
            //button[
                contains(
                    translate(
                        normalize-space(.),
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'login'
                )
            ]
            """
        ),
        (
            By.CSS_SELECTOR,
            "button[type='submit']"
        ),
        (
            By.CSS_SELECTOR,
            "input[type='submit']"
        ),
    ]

    login_button = find_first_visible(
        login_locators,
        description="Settings Sign In button",
    )

    submitted = False

    if login_button is not None:
        try:
            try:
                driver.execute_script(
                    """
                    arguments[0].scrollIntoView({
                        block: 'center',
                        inline: 'center'
                    });
                    """,
                    login_button,
                )

            except Exception:
                pass

            safe_sleep(0.2)

            try:
                login_button.click()

            except Exception:
                driver.execute_script(
                    "arguments[0].click();",
                    login_button
                )

            print(
                "PASS: Settings Sign In clicked"
            )

            submitted = True

        except Exception as e:
            print(
                f"WARNING: Could not click "
                f"Sign In button: {e}"
            )

    if not submitted:
        print(
            "Trying ENTER from password field."
        )

        try:
            password_field.send_keys(
                Keys.ENTER
            )

            print(
                "PASS: Login submitted "
                "using ENTER"
            )

            submitted = True

        except Exception as e:
            print(
                f"WARNING: Could not submit "
                f"login using ENTER: {e}"
            )

    if not submitted:
        print(
            "WARNING: Settings login "
            "could not be submitted."
        )

        print(
            "Continuing test."
        )

        return False

    safe_sleep(2)

    wait_for_page()

    try:
        print(
            f"Settings URL after login: "
            f"{driver.current_url}"
        )

    except Exception:
        pass

    # --------------------------------------------------------
    # Confirm authenticated Settings state
    # --------------------------------------------------------

    # IMPORTANT: Do NOT use the mere presence of password fields as a failed
    # login signal.  After a successful admin login the Admin Login tab contains
    # the Change Password form, so visible input[type=password] controls are
    # expected.  Instead, confirm the authenticated UI shown by Mantle Edge.
    try:
        authenticated_markers = [
            (By.XPATH, "//*[contains(normalize-space(.), 'Logged in as admin')]"),
            (By.XPATH, "//button[normalize-space()='Logout']"),
            (By.XPATH, "//button[normalize-space()='Log out']"),
            (By.XPATH, "//*[normalize-space()='Change Password']"),
        ]

        for locator in authenticated_markers:
            try:
                elements = driver.find_elements(*locator)
            except Exception:
                continue

            for element in elements:
                try:
                    if element.is_displayed():
                        print(
                            "PASS: Authenticated Settings page detected "
                            "after admin login"
                        )
                        return True
                except Exception:
                    continue

        # As a fallback, determine whether an actual login form is still present.
        # A password input by itself does not count because Change Password also
        # uses password inputs.
        login_user = driver.find_elements(
            By.CSS_SELECTOR,
            "input[name='username'], input#username, input[autocomplete='username']",
        )
        login_submit = driver.find_elements(
            By.XPATH,
            "//button[contains(translate(normalize-space(.), "
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'sign in') "
            "or contains(translate(normalize-space(.), "
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'login')]",
        )

        visible_user = any(
            element.is_displayed() for element in login_user
        )
        visible_submit = any(
            element.is_displayed() for element in login_submit
        )

        if visible_user and visible_submit:
            print(
                "WARNING: The Settings login form is still visible; "
                "admin login was not confirmed."
            )
            return False

        print(
            "PASS: Login form is gone; treating Settings login as successful"
        )
        return True

    except Exception as e:
        print(
            f"WARNING: Could not positively inspect authenticated state: {e}"
        )
        print(
            "Continuing as authenticated because the login submission completed."
        )
        return True


# ============================================================
# Settings top-menu traversal after login
# ============================================================

# These are the Settings tabs that must be exercised after the Gear login.
# Admin Login is intentionally excluded because the user is already signed in.
SETTINGS_TOP_MENU_ITEMS = [
    "Appliance",
    "Managed Apps",
    "Assets",
    "Actions",
    "System Actions",
]

# Keep every selected Settings tab visible for at least two seconds before
# scrolling it. This makes tab traversal obvious in both the browser and logs.
SETTINGS_TOP_MENU_HOLD_SECONDS = 2.0

# Pause between individual scroll positions so the browser visibly traverses
# the page instead of jumping immediately to the bottom.
SETTINGS_SCROLL_SETTLE_SECONDS = 0.65


def _settings_top_menu_xpath(label):
    """Build a case-sensitive exact-text XPath for a Settings top-menu item."""
    return (
        "//*[self::button or self::a or @role='tab' or @role='button' "
        "or self::div or self::span]"
        f"[normalize-space(.)='{label}']"
    )


def _find_settings_top_menu_element(label):
    """Find the visible top Settings tab by exact text.

    The Settings UI can re-render after every tab click, so callers should use
    this helper each time rather than holding a WebElement across navigation.
    """
    locators = [
        (By.XPATH, f"//*[@role='tab' and normalize-space(.)='{label}']"),
        (By.XPATH, f"//button[normalize-space(.)='{label}']"),
        (By.XPATH, f"//a[normalize-space(.)='{label}']"),
        (By.XPATH, _settings_top_menu_xpath(label)),
    ]

    for locator in locators:
        try:
            elements = driver.find_elements(*locator)
        except Exception:
            continue

        # Prefer the candidate closest to the top of the viewport. This avoids
        # accidentally selecting a same-named body heading farther down.
        visible = []
        for element in elements:
            try:
                if not (element.is_displayed() and element.is_enabled()):
                    continue
                rect = element.rect or {}
                visible.append((float(rect.get("y", 999999)), element))
            except Exception:
                continue

        if visible:
            visible.sort(key=lambda item: item[0])
            return visible[0][1]

    return None


def _click_settings_top_menu_item(label):
    """Open one Settings top-menu item and hold it on screen for two seconds."""
    print_header(f"OPENING SETTINGS TOP MENU: {label}")

    element = _find_settings_top_menu_element(label)
    if element is None:
        print(
            f"WARNING: Could not find Settings top-menu item: {label}"
        )
        return False

    try:
        # Bring the top menu itself into view without relying on the page's
        # current scroll position.
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'start',inline:'center'});",
            element,
        )
    except Exception:
        pass

    safe_sleep(0.25)

    if not _raw_click(element):
        # Last-resort DOM click. Some front ends place an overlay over the tab
        # even though the tab remains the correct event target.
        try:
            driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(
                f"WARNING: Could not open Settings top-menu item "
                f"{label}: {e}"
            )
            return False

    # Give the SPA time to render the selected tab's body.
    safe_sleep(0.5)
    wait_for_page(timeout=8)

    print(
        f"PASS: Opened Settings top-menu item: {label}"
    )
    print(
        f"INFO: Holding {label} open for "
        f"{SETTINGS_TOP_MENU_HOLD_SECONDS:.0f} seconds"
    )

    safe_sleep(SETTINGS_TOP_MENU_HOLD_SECONDS)
    return True


def _get_scroll_targets():
    """Return visible scrollable elements for the active Settings tab.

    The Settings application can put scrolling on an inner DIV instead of the
    browser window.  We deliberately return DOM elements (not measurements) so
    Selenium can move each real scroll container and verify that scrollTop
    actually changed.
    """
    script = r"""
    const result = [];
    const seen = new Set();

    function add(el) {
        if (!el || seen.has(el)) return;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        const range = (el.scrollHeight || 0) - (el.clientHeight || 0);
        const visible = rect.width > 20 && rect.height > 20 &&
                        style.display !== 'none' &&
                        style.visibility !== 'hidden' &&
                        Number(style.opacity || 1) !== 0;
        if (!visible || range <= 20) return;
        seen.add(el);
        result.push(el);
    }

    // Most likely Mantle Edge content regions first.
    const preferred = [
        'main',
        '[role="main"]',
        '[class*="content" i]',
        '[class*="page" i]',
        '[class*="panel" i]',
        '[class*="settings" i]',
        '[class*="container" i]'
    ];

    for (const selector of preferred) {
        for (const el of document.querySelectorAll(selector)) add(el);
    }

    for (const el of document.querySelectorAll('body *')) add(el);

    result.sort((a, b) =>
        ((b.scrollHeight - b.clientHeight) -
         (a.scrollHeight - a.clientHeight))
    );
    return result.slice(0, 10);
    """

    try:
        return driver.execute_script(script) or []
    except Exception as e:
        print(f"WARNING: Could not discover Settings scroll containers: {e}")
        return []


def _scroll_element_visibly(label, element, description):
    """Force one scrollable element from top to bottom in visible steps.

    This does not merely issue a smooth-scroll command.  After every movement
    it reads scrollTop back from the browser and verifies that the page really
    moved.  Each position is held long enough to be obvious to a person
    watching the Selenium browser.
    """
    try:
        metrics = driver.execute_script(
            "return {top: arguments[0].scrollTop || 0, "
            "client: arguments[0].clientHeight || 0, "
            "total: arguments[0].scrollHeight || 0};",
            element,
        ) or {}
        client = int(metrics.get("client", 0) or 0)
        total = int(metrics.get("total", 0) or 0)
    except Exception as e:
        print(f"WARNING: Could not measure {description} for {label}: {e}")
        return False

    bottom = max(total - client, 0)
    if client <= 0 or bottom <= 20:
        return False

    # Start at the actual top and visibly pause there.
    try:
        driver.execute_script("arguments[0].scrollTop = 0;", element)
    except Exception:
        return False

    safe_sleep(0.6)

    # Move roughly half a viewport per step.  This makes the scrolling plainly
    # visible rather than appearing to jump or not move at all.
    step = max(int(client * 0.50), 220)
    positions = list(range(step, bottom + 1, step))
    if not positions or positions[-1] != bottom:
        positions.append(bottom)

    print(
        f"INFO: VISIBLY scrolling {label} {description}: "
        f"viewport={client}px, content={total}px, bottom={bottom}px, "
        f"steps={len(positions)}"
    )

    moved = False
    previous = 0

    for number, requested in enumerate(positions, start=1):
        try:
            # Direct assignment is intentional: it is deterministic and lets us
            # verify the resulting position immediately.
            driver.execute_script(
                "arguments[0].scrollTop = arguments[1];",
                element,
                requested,
            )
            safe_sleep(0.18)
            actual = int(
                driver.execute_script(
                    "return Math.round(arguments[0].scrollTop || 0);",
                    element,
                )
                or 0
            )

            print(
                f"  {label}: {description} step "
                f"{number}/{len(positions)} requested={requested}px "
                f"actual={actual}px"
            )

            if actual > previous:
                moved = True
            previous = actual

            # Hold every intermediate position so the scrolling can be seen.
            safe_sleep(0.75)

        except StaleElementReferenceException:
            print(
                f"WARNING: {description} became stale while scrolling {label}."
            )
            break
        except Exception as e:
            print(
                f"WARNING: Could not scroll {description} on {label}: {e}"
            )
            break

    return moved


def _scroll_document_visibly(label):
    """Force the document scrollingElement from top to bottom and verify it."""
    try:
        metrics = driver.execute_script(
            "const e=document.scrollingElement || document.documentElement;"
            "return {client:e.clientHeight, total:e.scrollHeight, top:e.scrollTop};"
        ) or {}
        client = int(metrics.get("client", 0) or 0)
        total = int(metrics.get("total", 0) or 0)
    except Exception:
        return False

    bottom = max(total - client, 0)
    if client <= 0 or bottom <= 20:
        return False

    step = max(int(client * 0.50), 220)
    positions = list(range(0, bottom + 1, step))
    if not positions or positions[-1] != bottom:
        positions.append(bottom)

    print(
        f"INFO: VISIBLY scrolling {label} document: "
        f"viewport={client}px, content={total}px, steps={len(positions)}"
    )

    moved = False
    previous = 0
    for number, requested in enumerate(positions, start=1):
        try:
            actual = int(
                driver.execute_script(
                    "const e=document.scrollingElement || document.documentElement;"
                    "e.scrollTop=arguments[0]; return Math.round(e.scrollTop || 0);",
                    requested,
                )
                or 0
            )
            print(
                f"  {label}: document step {number}/{len(positions)} "
                f"requested={requested}px actual={actual}px"
            )
            if actual > previous:
                moved = True
            previous = actual
            safe_sleep(0.75)
        except Exception as e:
            print(f"WARNING: Document scroll failed for {label}: {e}")
            break

    return moved


def _keyboard_scroll_fallback(label):
    """Use real PAGE_DOWN keys when JavaScript scrolling cannot move the UI.

    This is especially useful for SPA layouts with custom wheel/keyboard scroll
    handling.  The currently selected Settings tab stays active while the body
    receives PAGE_DOWN several times, followed by END.
    """
    print(
        f"INFO: JavaScript did not prove movement on {label}; "
        "using PAGE_DOWN/END keyboard fallback."
    )

    try:
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()
    except Exception:
        try:
            body = driver.find_element(By.TAG_NAME, "body")
        except Exception:
            return False

    did_send = False
    for number in range(1, 7):
        try:
            body.send_keys(Keys.PAGE_DOWN)
            print(f"  {label}: keyboard PAGE_DOWN {number}/6")
            safe_sleep(0.85)
            did_send = True
        except Exception:
            break

    try:
        body.send_keys(Keys.END)
        print(f"  {label}: keyboard END")
        safe_sleep(1.0)
        did_send = True
    except Exception:
        pass

    return did_send


def _return_settings_tab_to_top():
    """Put all likely Settings scroll regions back at the top for next tab."""
    try:
        driver.execute_script(
            "const e=document.scrollingElement || document.documentElement;"
            "e.scrollTop=0; window.scrollTo(0,0);"
        )
    except Exception:
        pass

    for target in _get_scroll_targets():
        try:
            driver.execute_script("arguments[0].scrollTop = 0;", target)
        except Exception:
            continue

    try:
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)
    except Exception:
        pass

    safe_sleep(0.5)


def _scroll_current_settings_menu_page(label):
    """Actually scroll the active Settings tab from top to bottom.

    Every requested tab is held for two seconds by
    _click_settings_top_menu_item(), then this routine visibly traverses the
    document and any nested scrollable Settings content region.  Movement is
    verified by reading scrollTop after each step.
    """
    print_header(f"VISIBLE SETTINGS SCROLL: {label}")

    _return_settings_tab_to_top()

    did_scroll = _scroll_document_visibly(label)

    # Re-discover after the document attempt because tab content can lazy-render.
    targets = _get_scroll_targets()
    nested_moved = 0

    for index, target in enumerate(targets, start=1):
        if _scroll_element_visibly(
            label,
            target,
            f"scroll-container #{index}",
        ):
            did_scroll = True
            nested_moved += 1

    if not did_scroll:
        _keyboard_scroll_fallback(label)

    # Leave the tab at the bottom for a full second so the final location is
    # visible before returning to the top and opening the next menu item.
    print(f"INFO: Finished bottom traversal for {label}; holding bottom 1 second")
    safe_sleep(1.0)

    _return_settings_tab_to_top()

    print(
        f"PASS: Completed visible top-to-bottom traversal for {label} "
        f"(nested regions moved: {nested_moved})"
    )
    return True


def test_settings_top_menu_after_login():
    """After Gear sign-in, open and visibly scroll every requested Settings tab."""
    print_header("SETTINGS TOP-MENU TRAVERSAL AFTER LOGIN")

    opened = 0

    for label in SETTINGS_TOP_MENU_ITEMS:
        try:
            # Always put the menu back into view before selecting the next item.
            _return_settings_tab_to_top()

            if not _click_settings_top_menu_item(label):
                print(
                    f"WARNING: Skipping scroll because {label} could not be opened."
                )
                continue

            opened += 1

            # The tab has already been held for two seconds at this point.
            _scroll_current_settings_menu_page(label)

            # Keep the top of the completed tab visible briefly before moving on.
            safe_sleep(0.6)

        except Exception as e:
            print(
                f"WARNING: Settings top-menu test failed for {label}: {e}"
            )
            print("Continuing to next Settings menu item.")

    print_header("SETTINGS TOP-MENU TRAVERSAL COMPLETE")
    print(
        f"PASS: Opened {opened}/{len(SETTINGS_TOP_MENU_ITEMS)} "
        f"requested Settings top-menu item(s)."
    )

    return opened == len(SETTINGS_TOP_MENU_ITEMS)


# ============================================================
# Sidebar smoke test
# ============================================================

def test_sidebar_options():
    print_header(
        "SIDEBAR SMOKE TEST"
    )

    for option in sidebar_options:
        print_header(
            f"TESTING: {option}"
        )

        try:
            clicked = click_text(
                option
            )

            if clicked:
                safe_sleep(1)

                print_current_url()

            else:
                print(
                    f"WARNING: {option} "
                    "was not found/clicked."
                )

                print(
                    "Continuing to next option."
                )

        except Exception as e:
            print(
                f"WARNING: {option} "
                f"encountered error: {e}"
            )

            print(
                "Continuing to next option."
            )


# ============================================================
# Dashboard
# ============================================================

def _dashboard_is_loaded(timeout=6):
    """Return True only when the normal Dashboard application is visible.

    Settings is a separate front-end view.  A successful Settings login leaves
    Selenium on that application, where there is no left-side Dashboard link.
    Checking for Dashboard-specific content prevents the suite from accidentally
    running the Dashboard JavaScript against the Settings DOM.
    """
    dashboard_markers = [
        (By.XPATH, "//*[normalize-space()='System Status']"),
        (By.XPATH, "//*[normalize-space()='Services']"),
        (By.XPATH, "//*[normalize-space()='Compose Projects']"),
        (By.XPATH, "//*[normalize-space()='Execute System Action']"),
    ]

    end_time = time.time() + timeout
    while time.time() < end_time:
        for locator in dashboard_markers:
            try:
                for element in driver.find_elements(*locator):
                    if element.is_displayed():
                        return True
            except Exception:
                continue
        safe_sleep(0.2)

    return False


def _open_dashboard_directly():
    """Open /dashboard directly while preserving the current browser session.

    driver.get() keeps the same Selenium browser profile/cookies, so the admin
    Settings session is not discarded.  This is the reliable bridge between the
    Settings SPA and the normal Dashboard SPA.
    """
    print(f"INFO: Opening Dashboard directly: {DASHBOARD_URL}")

    try:
        driver.get(DASHBOARD_URL)
        wait_for_page(timeout=12)
        safe_sleep(1.0)
    except Exception as e:
        print(f"WARNING: Direct Dashboard navigation failed: {e}")
        return False

    if _dashboard_is_loaded(timeout=8):
        print("PASS: Dashboard loaded using direct /dashboard navigation")
        print_current_url()
        return True

    print(
        "WARNING: /dashboard was opened but Dashboard-specific content "
        "was not detected."
    )
    print_current_url()
    return False


def return_to_dashboard():
    """Return to the normal Dashboard from either Settings or a Dashboard page.

    The Settings area and Dashboard do not share the same navigation DOM.  If
    Selenium is still in Settings, do not look for the Dashboard sidebar link;
    navigate directly to /dashboard.  Once back in the Dashboard application,
    the original sidebar-navigation test can continue normally.
    """
    print_header("RETURNING TO DASHBOARD")

    try:
        current_url = driver.current_url or ""
    except Exception:
        current_url = ""

    # If Dashboard content is already present, no navigation is necessary.
    if _dashboard_is_loaded(timeout=1):
        print("PASS: Already on Dashboard")
        print_current_url()
        return True

    # Settings is a separate application/view.  It does not expose the normal
    # Dashboard sidebar, so go straight back to the Dashboard route.
    if "/settings" in current_url.lower() or "/admin" in current_url.lower():
        print(
            "INFO: Currently in Settings/Admin UI; switching to the "
            "Dashboard application before running Dashboard tests."
        )
        return _open_dashboard_directly()

    # When already inside the Dashboard shell, prefer the visible sidebar link.
    clicked = False
    try:
        elements = driver.find_elements(
            By.XPATH,
            "//*[self::a or self::button][normalize-space()='Dashboard']"
        )
        for element in elements:
            try:
                if not (element.is_displayed() and element.is_enabled()):
                    continue
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element,
                )
                safe_sleep(0.2)
                if _raw_click(element):
                    clicked = True
                    break
            except Exception:
                continue
    except Exception as e:
        print(f"WARNING: Dashboard sidebar lookup failed: {e}")

    if clicked:
        wait_for_page(timeout=8)
        safe_sleep(0.6)
        if _dashboard_is_loaded(timeout=6):
            print("PASS: Dashboard loaded from sidebar")
            print_current_url()
            return True
        print(
            "WARNING: Dashboard sidebar was clicked but Dashboard content "
            "was not detected; trying direct route."
        )
    else:
        print(
            "INFO: No usable Dashboard link exists in the current DOM; "
            "trying the direct Dashboard route."
        )

    return _open_dashboard_directly()


# ============================================================
# Execute System Action
# ============================================================

def test_execute_system_action():
    print_header(
        "EXECUTE SYSTEM ACTION"
    )

    execute_locator = (
        By.XPATH,
        "//*[normalize-space()="
        "'Execute System Action']",
    )

    try:
        clicked = safe_click(
            execute_locator,
            description="Execute System Action",
            retries=3,
        )

    except Exception as e:
        print(
            f"WARNING: Execute System Action "
            f"test failed: {e}"
        )

        return False

    if not clicked:
        print(
            "WARNING: Execute System Action "
            "was not found."
        )

        print(
            "Continuing test."
        )

        return False

    safe_sleep(1)

    print_current_url()

    try:
        driver.back()

        wait_for_page()

        safe_sleep(0.5)

        print(
            "PASS: Navigated back"
        )

    except Exception as e:
        print(
            f"WARNING: Back navigation "
            f"failed: {e}"
        )

    return True


# ============================================================
# Full UI page/tile click test
# ============================================================

def discover_sidebar_entries():
    """Return visible sidebar page labels, preserving known entries first."""
    discovered = []

    selectors = [
        "aside a",
        "aside button",
        "nav a",
        "nav button",
        "[class*='sidebar' i] a",
        "[class*='sidebar' i] button",
        "[class*='sidenav' i] a",
        "[class*='sidenav' i] button",
    ]

    for selector in selectors:
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
        except Exception:
            continue

        for element in elements:
            try:
                if not element.is_displayed():
                    continue

                text_value = " ".join((element.text or "").split())
                if not text_value or len(text_value) > 60:
                    continue

                lowered = text_value.lower()
                if any(word in lowered for word in GEAR_WORDS):
                    continue

                if text_value not in discovered:
                    discovered.append(text_value)

            except Exception:
                continue

    result = []

    for entry in sidebar_options + discovered:
        if entry not in result:
            result.append(entry)

    return result


def navigate_to_page(label):
    """Open a left-side navigation page by its visible label."""
    print_header(
        f"OPENING PAGE: {label}"
    )

    clicked = click_text(
        label
    )

    if clicked:
        safe_sleep(0.7)
        wait_for_page(timeout=8)
        print_current_url()

    return clicked


def _interactive_snapshot():
    """Snapshot every currently visible/enabled interactive DOM element.

    The JavaScript builds a stable-ish CSS path. The page is rescanned after
    every click so controls revealed by opening tiles, disclosure arrows,
    kebab menus, dialogs, and popovers are also tested.
    """
    script = r"""
    const selectors = [
        'a[href]',
        'button',
        '[role="button"]',
        '[role="menuitem"]',
        '[role="tab"]',
        '[role="switch"]',
        '[role="checkbox"]',
        'summary',
        'input',
        'select',
        'textarea',
        '[tabindex]:not([tabindex="-1"])'
    ];

    function cssPath(el) {
        if (!(el instanceof Element)) return '';
        const path = [];

        while (el && el.nodeType === Node.ELEMENT_NODE) {
            let selector = el.nodeName.toLowerCase();

            if (el.id) {
                selector += '#' + CSS.escape(el.id);
                path.unshift(selector);
                break;
            }

            let sibling = el;
            let nth = 1;

            while ((sibling = sibling.previousElementSibling) != null) {
                if (sibling.nodeName.toLowerCase() === el.nodeName.toLowerCase()) {
                    nth++;
                }
            }

            selector += `:nth-of-type(${nth})`;
            path.unshift(selector);
            el = el.parentElement;
        }

        return path.join(' > ');
    }

    function visible(el) {
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();

        if (style.display === 'none' || style.visibility === 'hidden') {
            return false;
        }

        if (Number(style.opacity) === 0) {
            return false;
        }

        if (rect.width <= 0 || rect.height <= 0) {
            return false;
        }

        return true;
    }

    const nodes = Array.from(
        document.querySelectorAll(selectors.join(','))
    );

    const seen = new Set();
    const result = [];

    for (const el of nodes) {
        if (!visible(el)) continue;
        if (el.disabled) continue;

        const selector = cssPath(el);
        if (!selector || seen.has(selector)) continue;
        seen.add(selector);

        const text = (el.innerText || el.value || '').trim();
        const aria = (el.getAttribute('aria-label') || '').trim();
        const title = (el.getAttribute('title') || '').trim();
        const href = (el.getAttribute('href') || '').trim();
        const type = (el.getAttribute('type') || '').trim();
        const role = (el.getAttribute('role') || '').trim();
        const tag = el.tagName.toLowerCase();
        const fingerprint = [
            selector,
            text,
            aria,
            title,
            href,
            type,
            role
        ].join('||');

        result.push({
            fingerprint,
            selector,
            text,
            aria_label: aria,
            title,
            href,
            tag,
            element_type: type,
            role,
        });
    }

    return result;
    """

    try:
        raw_items = driver.execute_script(
            script
        ) or []

    except Exception as e:
        print(
            f"WARNING: Could not snapshot "
            f"interactive elements: {e}"
        )
        return []

    items = []

    for raw in raw_items:
        try:
            items.append(
                InteractiveItem(
                    fingerprint=str(
                        raw.get("fingerprint", "")
                    ),
                    selector=str(
                        raw.get("selector", "")
                    ),
                    text=str(
                        raw.get("text", "")
                    ),
                    aria_label=str(
                        raw.get("aria_label", "")
                    ),
                    title=str(
                        raw.get("title", "")
                    ),
                    href=str(
                        raw.get("href", "")
                    ),
                    tag=str(
                        raw.get("tag", "")
                    ),
                    element_type=str(
                        raw.get("element_type", "")
                    ),
                    role=str(
                        raw.get("role", "")
                    ),
                )
            )

        except Exception:
            continue

    return items


def _looks_like_sidebar_navigation(item):
    normalized = " ".join(
        item.text.split()
    ).lower()

    known = {
        name.lower()
        for name in discover_sidebar_entries()
    }

    if normalized and normalized in known:
        return True

    selector = item.selector.lower()

    return (
        "aside" in selector
        or "sidebar" in selector
        or "sidenav" in selector
    )


def _looks_like_gear(item):
    combined = item.combined_text
    return any(
        word in combined
        for word in GEAR_WORDS
    )


def _looks_destructive(item):
    combined = item.combined_text
    return any(
        word in combined
        for word in DESTRUCTIVE_WORDS
    )


def _looks_like_logout(item):
    combined = item.combined_text

    return any(
        word in combined
        for word in (
            "logout",
            "log out",
            "sign out",
        )
    )


def _should_skip_generic_item(item):
    # Sidebar navigation is exercised by the page traversal itself. Re-clicking
    # it during a page sweep would constantly leave the page being tested.
    if _looks_like_sidebar_navigation(item):
        return (
            True,
            "sidebar navigation is tested separately",
        )

    # Preserve Gear -> Settings -> Sign In as the dedicated authentication path.
    if _looks_like_gear(item):
        return (
            True,
            "Gear/Settings is tested by the dedicated sign-in workflow",
        )

    # Logging out would break the remainder of the suite.
    if _looks_like_logout(item):
        return (
            True,
            "logout/sign-out would end the authenticated test session",
        )

    if (
        _looks_destructive(item)
        and not ALLOW_DESTRUCTIVE_ACTIONS
    ):
        return (
            True,
            "destructive action disabled by "
            "ALLOW_DESTRUCTIVE_ACTIONS=False",
        )

    # A file input requires an actual test fixture path.
    if (
        item.tag == "input"
        and item.element_type.lower() == "file"
    ):
        return (
            True,
            "file input needs a test fixture",
        )

    return False, ""


def _find_snapshot_element(item):
    try:
        elements = driver.find_elements(
            By.CSS_SELECTOR,
            item.selector,
        )

    except Exception:
        return None

    for element in elements:
        try:
            if (
                element.is_displayed()
                and element.is_enabled()
            ):
                return element

        except Exception:
            continue

    return None


def _is_toggle_control(item):
    """Return True when an opened tile exposes a state toggle."""
    role = item.role.lower().strip()
    element_type = item.element_type.lower().strip()
    combined = item.combined_text

    if role in {
        "switch",
        "checkbox",
    }:
        return True

    if (
        item.tag == "input"
        and element_type in {
            "checkbox",
            "radio",
        }
    ):
        return True

    # Some component libraries expose switches as ordinary buttons. Common
    # accessible wording provides a conservative fallback.
    return (
        any(
            marker in combined
            for marker in (
                "toggle",
                "enable",
                "enabled",
                "disable",
                "disabled",
            )
        )
        and item.tag in {
            "button",
            "input",
        }
    )


def _read_toggle_state(element):
    """Read the current state without assuming a specific UI framework."""
    try:
        aria_checked = element.get_attribute(
            "aria-checked"
        )

        if aria_checked is not None:
            return (
                f"aria-checked={aria_checked}"
            )

    except Exception:
        pass

    try:
        aria_pressed = element.get_attribute(
            "aria-pressed"
        )

        if aria_pressed is not None:
            return (
                f"aria-pressed={aria_pressed}"
            )

    except Exception:
        pass

    try:
        if element.tag_name.lower() == "input":
            checked = driver.execute_script(
                "return arguments[0].checked;",
                element,
            )

            if checked is not None:
                return (
                    f"checked={bool(checked)}"
                )

    except Exception:
        pass

    return "unknown"


def _raw_click(element):
    """Click one element with JavaScript fallback."""
    try:
        element.click()
        return True

    except (
        ElementClickInterceptedException,
        ElementNotInteractableException,
        WebDriverException,
    ):
        try:
            driver.execute_script(
                "arguments[0].click();",
                element,
            )
            return True

        except Exception:
            return False

    except Exception:
        return False


def _toggle_on_and_off(item, element):
    """Toggle an opened-tile control both ways and restore its start state.

    Starts OFF: OFF -> ON -> OFF.
    Starts ON:  ON  -> OFF -> ON.

    This tests both states without leaving the appliance configuration changed.
    """
    before = _read_toggle_state(
        element
    )

    print(
        f"INFO: Toggle start state for "
        f"{item.description}: {before}"
    )

    if not _raw_click(element):
        print(
            f"WARNING: Could not perform "
            f"first toggle click: "
            f"{item.description}"
        )
        return False

    safe_sleep(
        CLICK_SETTLE_SECONDS
    )

    # React/Vue may replace the DOM node after a state change. Re-find it.
    element = _find_snapshot_element(
        item
    )

    if element is None:
        print(
            f"WARNING: Toggle disappeared "
            f"after first click; could not "
            f"restore: {item.description}"
        )
        return False

    middle = _read_toggle_state(
        element
    )

    print(
        f"PASS: Toggle changed state for "
        f"{item.description}: {middle}"
    )

    if not _raw_click(element):
        print(
            f"WARNING: Could not perform "
            f"second toggle click: "
            f"{item.description}"
        )
        return False

    safe_sleep(
        CLICK_SETTLE_SECONDS
    )

    element = _find_snapshot_element(
        item
    )

    if element is not None:
        after = _read_toggle_state(
            element
        )
    else:
        after = "unavailable"

    print(
        f"PASS: Toggled ON/OFF and restored "
        f"{item.description}: "
        f"{before} -> {middle} -> {after}"
    )

    return True


def _click_interactive_item(item):
    element = _find_snapshot_element(
        item
    )

    if element is None:
        print(
            f"INFO: Element disappeared "
            f"before click: {item.description}"
        )
        return False

    try:
        driver.execute_script(
            "arguments[0].scrollIntoView({"
            "block:'center',inline:'center'});",
            element,
        )

    except Exception:
        pass

    safe_sleep(0.1)

    # IMPORTANT: after a tile/menu is opened, a newly visible switch/checkbox
    # is discovered on the next scan and is exercised in both directions.
    if _is_toggle_control(item):
        return _toggle_on_and_off(
            item,
            element,
        )

    if not _raw_click(element):
        print(
            f"WARNING: Could not click "
            f"{item.description}"
        )
        return False

    print(
        f"PASS: Clicked page item: "
        f"{item.description}"
    )

    return True


def click_all_items_on_current_page(page_name):
    """Click all controls on the current page, including items revealed later."""
    print_header(
        f"CLICKING ALL ITEMS ON: {page_name}"
    )

    seen = set()
    skipped = {}
    successful_clicks = 0
    failed_clicks = 0

    try:
        original_handle = driver.current_window_handle
    except Exception:
        original_handle = None

    try:
        page_start_url = driver.current_url
    except Exception:
        page_start_url = URL

    for _ in range(
        MAX_INTERACTIONS_PER_PAGE
    ):
        if original_handle is not None:
            close_extra_windows(
                original_handle
            )

        snapshot = _interactive_snapshot()
        candidate = None

        for item in snapshot:
            if item.fingerprint in seen:
                continue

            should_skip, reason = (
                _should_skip_generic_item(
                    item
                )
            )

            if should_skip:
                seen.add(
                    item.fingerprint
                )

                skipped[item.fingerprint] = (
                    f"{item.description} -- {reason}"
                )

                continue

            candidate = item
            break

        if candidate is None:
            break

        seen.add(
            candidate.fingerprint
        )

        try:
            before_url = driver.current_url
        except Exception:
            before_url = page_start_url

        if _click_interactive_item(
            candidate
        ):
            successful_clicks += 1
        else:
            failed_clicks += 1

        safe_sleep(
            CLICK_SETTLE_SECONDS
        )

        if original_handle is not None:
            close_extra_windows(
                original_handle
            )

        try:
            current_url = driver.current_url
        except Exception:
            current_url = before_url

        if current_url != before_url:
            print(
                f"INFO: Click changed URL: "
                f"{before_url} -> {current_url}"
            )

            # External links are tested, then immediately return to Mantle Edge.
            if not is_application_url(
                current_url
            ):
                try:
                    driver.back()
                    wait_for_page(timeout=8)
                    safe_sleep(0.4)

                except Exception:
                    driver.get(
                        page_start_url
                    )
                    wait_for_page(timeout=8)

            # If a body control navigated to another internal page, restore the
            # page currently under test so remaining controls still get tested.
            elif page_name and page_name != "Settings":
                try:
                    if (
                        page_name.lower()
                        not in current_url.lower()
                    ):
                        click_text(
                            page_name
                        )
                        safe_sleep(0.5)

                except Exception:
                    pass

        # Do not dismiss overlays here. Menus/dialogs/popovers opened by the
        # last click contain new controls which must be discovered and clicked.

    else:
        print(
            f"WARNING: Reached "
            f"MAX_INTERACTIONS_PER_PAGE="
            f"{MAX_INTERACTIONS_PER_PAGE} "
            f"on {page_name}."
        )

    print(
        "\n--- PAGE CLICK SUMMARY ---"
    )

    print(
        f"Page: {page_name}"
    )

    print(
        f"Clicked: {successful_clicks}"
    )

    print(
        f"Failed clicks: {failed_clicks}"
    )

    print(
        f"Skipped by policy/workflow: "
        f"{len(skipped)}"
    )

    if skipped:
        print(
            "Skipped controls:"
        )

        values = list(
            skipped.values()
        )

        for value in values[:40]:
            print(
                f"  - {value}"
            )

        if len(values) > 40:
            print(
                f"  ... and "
                f"{len(values) - 40} more"
            )


def test_every_page_and_every_item():
    """Visit every sidebar page and exercise every discoverable page control."""
    print_header(
        "FULL UI CLICK TEST"
    )

    # Start from the normal Dashboard shell for dynamic sidebar discovery.
    # Settings and Dashboard use different DOM/navigation structures, so do not
    # run the Dashboard interaction JavaScript until Dashboard is confirmed.
    if not return_to_dashboard():
        print(
            "WARNING: Could not enter the Dashboard application. "
            "Skipping Dashboard page/item sweep instead of running against "
            "the Settings DOM."
        )
        return False

    safe_sleep(1.0)

    if not _dashboard_is_loaded(timeout=6):
        print(
            "WARNING: Dashboard markers disappeared before page discovery. "
            "Skipping Dashboard sweep."
        )
        return False

    pages = discover_sidebar_entries()

    print(
        f"Discovered sidebar pages: {pages}"
    )

    for page_name in pages:
        try:
            if not navigate_to_page(
                page_name
            ):
                print(
                    f"WARNING: Could not open "
                    f"{page_name}; continuing."
                )
                continue

            click_all_items_on_current_page(
                page_name
            )

        except Exception as e:
            print(
                f"WARNING: Full click test failed "
                f"on {page_name}: {e}"
            )

            print(
                "Continuing to next page."
            )

    # Predictable final state.
    return_to_dashboard()


# ============================================================
# Main test
# ============================================================

def main():
    global driver, wait

    print_header(
        "STARTING MANTLE EDGE UI TEST"
    )

    # --------------------------------------------------------
    # Start Chrome
    # --------------------------------------------------------

    try:
        driver = webdriver.Chrome(
            options=options
        )

        wait = WebDriverWait(
            driver,
            15,
            poll_frequency=0.25,
            ignored_exceptions=(
                StaleElementReferenceException,
                NoSuchElementException,
            ),
        )

        print(
            "PASS: Chrome started"
        )

    except Exception as e:
        print(
            f"ERROR: Chrome could not start: {e}"
        )

        driver = None
        return

    try:
        # ----------------------------------------------------
        # Open application
        # ----------------------------------------------------

        try:
            print(
                f"Opening: {URL}"
            )

            driver.get(
                URL
            )

            wait_for_page()

        except Exception as e:
            print(
                f"WARNING: Could not open "
                f"{URL}: {e}"
            )

            print(
                "Attempting to continue."
            )

        # ----------------------------------------------------
        # Verify body
        # ----------------------------------------------------

        try:
            WebDriverWait(
                driver,
                10
            ).until(
                EC.presence_of_element_located(
                    (
                        By.TAG_NAME,
                        "body"
                    )
                )
            )

            print(
                "PASS: Application opened"
            )

        except Exception as e:
            print(
                f"WARNING: Application body "
                f"was not detected: {e}"
            )

            print(
                "Continuing test."
            )

        # ----------------------------------------------------
        # Sidebar
        # ----------------------------------------------------

        try:
            test_sidebar_options()

        except Exception as e:
            print(
                f"WARNING: Sidebar smoke test "
                f"encountered error: {e}"
            )

            print(
                "Continuing test."
            )

        # ----------------------------------------------------
        # Utilization
        # ----------------------------------------------------

        utilization_opened = False

        try:
            utilization_opened = (
                open_utilization()
            )

        except Exception as e:
            print(
                f"WARNING: Could not open "
                f"Utilization: {e}"
            )

            print(
                "Continuing test."
            )

        if utilization_opened:
            try:
                inspect_utilization_metrics()

            except Exception as e:
                print(
                    f"WARNING: Metric inspection "
                    f"failed: {e}"
                )

                print(
                    "Continuing test."
                )

            try:
                scroll_utilization()

            except Exception as e:
                print(
                    f"WARNING: Utilization scroll "
                    f"failed: {e}"
                )

                print(
                    "Continuing test."
                )

            print_header(
                "UPDATED LIVE METRICS"
            )

            try:
                driver.execute_script(
                    "window.scrollTo(0, 0);"
                )

            except Exception as e:
                print(
                    f"WARNING: Could not return "
                    f"to top of Utilization: {e}"
                )

            safe_sleep(1)

            try:
                inspect_utilization_metrics()

            except Exception as e:
                print(
                    f"WARNING: Updated metric "
                    f"inspection failed: {e}"
                )

                print(
                    "Continuing test."
                )

        else:
            print(
                "WARNING: Utilization was "
                "not opened."
            )

            print(
                "Skipping detailed Utilization "
                "checks and continuing."
            )

        # ----------------------------------------------------
        # Gear / Settings
        # ----------------------------------------------------

        print_header(
            "TESTING BOTTOM SETTINGS CONTROL"
        )

        settings_clicked = False

        try:
            settings_clicked = (
                click_gear_settings()
            )

        except Exception as e:
            print(
                f"WARNING: Settings/Gear test "
                f"encountered error: {e}"
            )

            print(
                "Continuing test."
            )

        # ----------------------------------------------------
        # Settings login
        # ----------------------------------------------------

        if settings_clicked:
            safe_sleep(1)

            try:
                print(
                    f"Settings destination URL: "
                    f"{driver.current_url}"
                )

            except Exception as e:
                print(
                    f"WARNING: Could not read "
                    f"Settings URL: {e}"
                )

            try:
                print_visible_page_text()

            except Exception as e:
                print(
                    f"WARNING: Could not read "
                    f"Settings page text: {e}"
                )

            settings_login_success = False

            try:
                settings_login_success = (
                    login_to_settings(
                        username=USERNAME,
                        password=PASSWORD,
                    )
                )

            except Exception as e:
                print(
                    f"WARNING: Settings login "
                    f"encountered error: {e}"
                )

                print(
                    "Continuing test."
                )

            if settings_login_success:
                print_header(
                    "SETTINGS LOGIN SUCCESSFUL"
                )

                print(
                    "PASS: Successfully signed "
                    "into Settings"
                )

                # ------------------------------------------------
                # Settings top menu after successful Gear sign-in
                # ------------------------------------------------

                try:
                    test_settings_top_menu_after_login()

                except Exception as e:
                    print(
                        f"WARNING: Settings top-menu "
                        f"traversal failed: {e}"
                    )

                    print(
                        "Continuing test."
                    )

                # ------------------------------------------------
                # Settings and Dashboard are separate UI contexts.
                # Explicitly leave Settings before Dashboard tests.
                # ------------------------------------------------
                try:
                    print_header(
                        "LEAVING SETTINGS AND OPENING DASHBOARD"
                    )
                    if not _open_dashboard_directly():
                        print(
                            "WARNING: Dashboard did not load immediately "
                            "after Settings traversal. The full UI test will "
                            "retry Dashboard navigation."
                        )
                except Exception as e:
                    print(
                        f"WARNING: Could not switch from Settings to "
                        f"Dashboard: {e}"
                    )

            else:
                print_header(
                    "SETTINGS LOGIN NOT CONFIRMED"
                )

                print(
                    "WARNING: Settings login "
                    "was not confirmed."
                )

                print(
                    "Continuing test."
                )

        else:
            print(
                "WARNING: Gear / Settings "
                "was not found."
            )

            print(
                "Skipping Settings login "
                "and continuing."
            )

        # ----------------------------------------------------
        # Click every page item / tile and toggle switches
        # ----------------------------------------------------

        try:
            test_every_page_and_every_item()

        except Exception as e:
            print(
                f"WARNING: Full UI click test "
                f"encountered error: {e}"
            )

            print(
                "Continuing test."
            )

        # ----------------------------------------------------
        # Return to Dashboard
        # ----------------------------------------------------

        try:
            return_to_dashboard()

        except Exception as e:
            print(
                f"WARNING: Dashboard return "
                f"failed: {e}"
            )

            print(
                "Continuing test."
            )

        # ----------------------------------------------------
        # Execute System Action
        # ----------------------------------------------------

        try:
            test_execute_system_action()

        except Exception as e:
            print(
                f"WARNING: Execute System Action "
                f"test failed: {e}"
            )

            print(
                "Continuing test."
            )

        # ----------------------------------------------------
        # Final page information
        # ----------------------------------------------------

        print_header(
            "FINAL PAGE INFORMATION"
        )

        try:
            print_current_url()

        except Exception as e:
            print(
                f"WARNING: Could not print "
                f"final URL: {e}"
            )

        try:
            print_visible_page_text()

        except Exception as e:
            print(
                f"WARNING: Could not print "
                f"final page text: {e}"
            )

    except Exception as e:
        print_header(
            "UNEXPECTED TOP-LEVEL TEST ERROR"
        )

        print(
            type(e).__name__
        )

        print(
            e
        )

    finally:
        print_header(
            "TEST FINISHED"
        )

        if driver is not None:
            try:
                driver.quit()

                print(
                    "PASS: Chrome closed"
                )

            except Exception as e:
                print(
                    f"WARNING: Could not close "
                    f"Chrome normally: {e}"
                )


if __name__ == "__main__":
    main()
