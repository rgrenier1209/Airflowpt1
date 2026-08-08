import sys
import argparse
from pathlib import Path


def analyze_file(file, level="ERROR"):
    """
    Parses an individual log file to count and collect lines matching a status level.
    
    Args:
        file (Path/str): Path to the log file.
        level (str): The log status keyword to filter by (e.g., ERROR, WARNING, INFO).
        
    Returns:
        count (int): Number of matching log entries in this file.
        cur_list (list): List of matching log lines found.
    """
    count = 0
    cur_list = []
    target_keyword = level.upper()

    try:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                # Case-insensitive check for the target keyword
                if target_keyword in line.upper():
                    count += 1
                    cur_list.append(line.strip())
    except Exception as e:
        print(f"Error reading file {file}: {e}")

    return count, cur_list


def main():
    parser = argparse.ArgumentParser(
        description="Recursively analyze Airflow log files for specific statuses (ERROR, WARNING, INFO, etc.)."
    )
    parser.add_argument(
        "log_dir",
        type=str,
        help="Path to the directory containing log files."
    )
    parser.add_argument(
        "--level", "-l",
        type=str,
        default="ERROR",
        help="Log level to search for (e.g., WARNING, ERROR, INFO). Default is ERROR."
    )

    args = parser.parse_args()

    log_dir = Path(args.log_dir)

    if not log_dir.exists() or not log_dir.is_dir():
        print(f"Error: Directory '{log_dir}' does not exist or is not a directory.")
        sys.exit(1)

    file_list = list(log_dir.rglob("*.log"))

    total_count = 0
    all_entries = []

    for file in file_list:
        count, cur_list = analyze_file(file, level=args.level)
        total_count += count
        all_entries.extend(cur_list)

    status_label = args.level.upper()
    print(f"Total number of {status_label} entries: {total_count}")
    if total_count > 0:
        print(f"\nHere are all the {status_label} entries:")
        for entry in all_entries:
            print(entry)


if __name__ == "__main__":
    main()