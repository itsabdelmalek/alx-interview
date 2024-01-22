#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':
    filesize, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats_count = {k: 0 for k in status_codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()

            # Update status code count
            try:
                current_status_code = data[-2]
                if current_status_code in stats_count:
                    stats_count[current_status_code] += 1
            except IndexError:
                pass

            # Update file size
            try:
                filesize += int(data[-1])
            except (ValueError, IndexError):
                pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(stats_count, filesize)

        # Print final stats
        print_stats(stats_count, filesize)

    except KeyboardInterrupt:
        print_stats(stats_count, filesize)
        raise
