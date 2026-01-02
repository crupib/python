#!/usr/bin/env python3
"""
download_debs.py

Downloads the main package and all of its dependencies as .deb files
for Ubuntu 22.04 LTS by enumerating dependencies via apt-rdepends.
Filters out virtual packages (those without a candidate version).

Usage:
  chmod +x download_debs.py
  ./download_debs.py -p <package> -d <dest_dir>
"""

import subprocess
import argparse
import shutil
import sys
from pathlib import Path


def check_command(cmd):
    """Ensure the given command is available on PATH."""
    if shutil.which(cmd) is None:
        print(f"Error: '{cmd}' not found. Please install it and try again.")
        sys.exit(1)


def is_real_package(pkg):
    """Check if a package has a candidate version (i.e., not virtual)."""
    try:
        output = subprocess.check_output(["apt-cache", "policy", pkg], text=True)
    except subprocess.CalledProcessError:
        return False
    for line in output.splitlines():
        line = line.strip()
        if line.startswith('Candidate:'):
            cand = line.split(':', 1)[1].strip()
            return bool(cand) and cand != '(none)'
    return False


def get_dependencies(package):
    """Return a list of all real dependencies (Depends & PreDepends)."""
    try:
        output = subprocess.check_output(["apt-rdepends", package], text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: apt-rdepends failed for {package}: {e}")
        sys.exit(1)

    deps = []
    seen = set()
    # Include the root package first
    deps.append(package)
    seen.add(package)

    for line in output.splitlines():
        line = line.strip()
        if line.startswith(('Depends:', 'PreDepends:')):
            parts = line.split()
            if len(parts) < 2:
                continue
            pkg = parts[1]
            if pkg not in seen:
                seen.add(pkg)
                deps.append(pkg)

    real_deps = []
    for pkg in deps:
        if is_real_package(pkg):
            real_deps.append(pkg)
        else:
            print(f"[-] Skipping virtual or no-candidate package: {pkg}")
    return real_deps


def prepare_dest(dest_dir):
    """Create a clean destination directory and return its Path."""
    p = Path(dest_dir).expanduser().resolve()
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True)
    return p


def download_packages(packages, dest):
    """Download each .deb via apt-get download into dest."""
    for pkg in packages:
        print(f"[+] Downloading {pkg}...")
        try:
            subprocess.check_call(["apt-get", "download", pkg], cwd=str(dest))
        except subprocess.CalledProcessError as e:
            print(f"Warning: failed to download {pkg}: {e}")
    print("[+] All packages downloaded to {dest}.")


def main():
    parser = argparse.ArgumentParser(
        description="Download a package and all its real dependencies as .deb files."
    )
    parser.add_argument(
        "-p", "--package", required=True,
        help="Package name to download (e.g., firefox or ubuntu-desktop)"
    )
    parser.add_argument(
        "-d", "--dest", default="deb-downloads",
        help="Destination directory for .deb files"
    )
    args = parser.parse_args()

    # Ensure required tools are installed
    check_command("apt-rdepends")
    check_command("apt-cache")
    check_command("apt-get")

    # Get filtered dependency list
    print(f"[+] Resolving dependencies for {args.package}...")
    deps = get_dependencies(args.package)

    # Prepare output folder
    dest = prepare_dest(args.dest)

    # Download each .deb
    download_packages(deps, dest)

if __name__ == "__main__":
    main()
