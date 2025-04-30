#!/usr/bin/env python3
import argparse
import os
import time
import shutil
import filecmp
import subprocess

def backup_file(src, dst):
    """
    Copy the source file to the destination (backup) file.
    """
    shutil.copy2(src, dst)
    print(f"Backup created: '{dst}'")

def file_has_changed(original, backup):
    """
    Compare the original file with the backup.
    Returns True if they differ.
    """
    # shallow=False ensures that file contents are compared
    return not filecmp.cmp(original, backup, shallow=False)

def monitor_file(file_path, backup_path, command, interval, oneshot):
    """
    Monitor file for changes.
    
    - Makes an initial backup of the file.
    - Then (either once or continuously) waits for the given interval,
      compares the file to its backup, and if it has changed, runs the command.
    - If running continuously, the backup is updated after the command runs.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    # Create an initial backup of the file
    backup_file(file_path, backup_path)

    if oneshot:
        print(f"Waiting {interval} seconds for a potential update...")
        time.sleep(interval)
        if file_has_changed(file_path, backup_path):
            print("File change detected!")
            subprocess.run(command, shell=True)
        else:
            print("No change detected.")
    else:
        print(f"Monitoring '{file_path}' every {interval} seconds. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(interval)
                if file_has_changed(file_path, backup_path):
                    print("File change detected!")
                    subprocess.run(command, shell=True)
                    # Update backup after change is handled
                    backup_file(file_path, backup_path)
                else:
                    print("No change detected.")
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Backup a file, monitor it for changes, and run a command if it changes."
    )
    parser.add_argument("file", help="Path to the file to monitor")
    parser.add_argument("command", help="Command to run if a change is detected (quote if needed)")
    parser.add_argument(
        "--backup",
        default=None,
        help="Path for the backup file (default: original filename with '.bak' appended)",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=5,
        help="Polling interval in seconds (default: 5 seconds)",
    )
    parser.add_argument(
        "--oneshot",
        action="store_true",
        help="Check for a change once after the interval then exit",
    )

    args = parser.parse_args()
    backup_file_path = args.backup if args.backup else args.file + ".bak"
    monitor_file(args.file, backup_file_path, args.command, args.interval, args.oneshot)

