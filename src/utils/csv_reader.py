import csv
import sys


def csv_reader(path):
    if not path.endswith(".csv"):
        print("invalid file type", file=sys.stderr)
    try:
        with open(path, "r") as file:
            csvreader = csv.reader(file)
            return csvreader
    except FileNotFoundError:
        raise FileNotFoundError(f'File referring to "{path}" not found.')
