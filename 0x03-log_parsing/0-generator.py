#!/usr/bin/python3
import sys
import signal

def print_statistics(total_size, status_codes):
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

def process_line(line, total_size, status_codes):
    try:
        parts = line.split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
        return total_size, status_codes
    except (ValueError, IndexError):
        return total_size, status_codes

def main():
    total_size = 0
    status_codes = {}
    lines_processed = 0

    try:
        for line in sys.stdin:
            lines_processed += 1
            total_size, status_codes = process_line(line.strip(), total_size, status_codes)

            if lines_processed % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

