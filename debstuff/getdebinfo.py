#!/usr/bin/env python3
import os
import re
import subprocess
import argparse

def get_control_field(deb_path, field):
    """
    Returns the contents of a control field (e.g. 'Package', 'Depends') for the given .deb,
    or an empty string if the field is not present.
    """
    try:
        out = subprocess.check_output(
            ["dpkg-deb", "--field", deb_path, field],
            stderr=subprocess.DEVNULL,
            encoding="utf-8",
        ).strip()
        return out
    except subprocess.CalledProcessError:
        return ""

def parse_depends_field(dep_str):
    """
    Splits a Debian dependency string into individual package names.
    E.g. "libc6 (>= 2.31), libssl1.1" → ["libc6", "libssl1.1"]
    """
    names = []
    for token in dep_str.split(","):
        token = token.strip()
        if not token:
            continue
        # take everything up to the first space or '('
        name = re.split(r"[ \(]", token)[0]
        names.append(name)
    return names

def classify_debs(directory):
    # find all .deb files
    debs = [f for f in os.listdir(directory) if f.endswith(".deb")]
    pkg_deps = {}

    # extract Package name and its dependencies
    for deb in debs:
        path = os.path.join(directory, deb)
        pkg_name = get_control_field(path, "Package")
        if not pkg_name:
            continue

        deps = []
        for fld in ("Pre-Depends", "Depends"):
            fld_val = get_control_field(path, fld)
            if fld_val:
                deps.extend(parse_depends_field(fld_val))
        pkg_deps[pkg_name] = deps

    all_pkgs = set(pkg_deps)
    depended_on = set(d for deps in pkg_deps.values() for d in deps if d in all_pkgs)

    main_pkgs = sorted(all_pkgs - depended_on)
    dep_pkgs  = sorted(depended_on)

    return main_pkgs, dep_pkgs

def main():
    parser = argparse.ArgumentParser(
        description="Classify .deb files into top-level packages vs. dependencies."
    )
    parser.add_argument(
        "dir",
        nargs="?",
        default=".",
        help="Directory containing .deb files (default: current directory)"
    )
    args = parser.parse_args()

    mains, deps = classify_debs(args.dir)

    print("=== Main (top‑level) packages ===")
    for p in mains:
        print(p)
    print("\n=== Dependencies ===")
    for p in deps:
        print(p)

if __name__ == "__main__":
    main()
