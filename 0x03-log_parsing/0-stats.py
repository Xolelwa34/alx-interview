#!/usr/bin/env python3
"""
Log parsing script that reads input line by line and computes metrics.
"""

import sys

# Initialize counters and storage
total_size = 0
status_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        try:
            # Split line into parts based on the required format
            parts = line.split()
            # Validate the line format (IP - [date] "GET /projects/260 HTTP/1.1" status_code file_size)
            if len(parts) < 7:
                continue

            # Extract status code and file size
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code count if it's a valid code
            if status_code in status_count:
                status_count[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines with incorrect format or invalid data
            continue

        # Increment line count
        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interruption
    print_stats()
    raise

# Print any remaining stats at the end of input
print_stats()

