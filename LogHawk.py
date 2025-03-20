import re
import argparse
from collections import Counter

# Default regex pattern
DEFAULT_REGEX = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\S+) (.*)'

# Set up argument parser
parser = argparse.ArgumentParser(description="Parse log files with a custom regex pattern.")
parser.add_argument("logfile", help="Path to the log file")
parser.add_argument("--regex", help="Custom regex pattern (default is a generic log format)", default=DEFAULT_REGEX)

args = parser.parse_args()

# Compile regex pattern
try:
    pattern = re.compile(args.regex)
except re.error:
    print("Invalid regex pattern. Using default.")
    pattern = re.compile(DEFAULT_REGEX)

# Read log file
event_lines = []

try:
    with open(args.logfile, 'r') as infile:
        for line in infile:
            match = pattern.search(line)
            if match:
                event_lines.append(match)

    # Count total number of events
    event_count = len(event_lines)
    print(f'{event_count} total events found in source file')

    # Breakdown by user
    users = [l.group(2) for l in event_lines]  # Assuming group(2) is the user
    user_count = Counter(users)
    print('\nBreakdown by user:')
    for user, count in user_count.items():
        print(f'{user} - {count}')

    # Write a timeline file
    with open('timeline.txt', 'w') as outfile:
        outfile.writelines([f'{l.group(1)} - {l.group(2)} - {l.group(3)}\n' for l in event_lines])

    print("\nLog analysis complete. Timeline saved as 'timeline.txt'.")

except FileNotFoundError:
    print(f"Error: The file '{args.logfile}' was not found. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")