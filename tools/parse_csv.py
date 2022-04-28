#!/usr/bin/env python3
"""
A simple tool to parse list of active domain names from MFCR blocklist CSV

Author: Ondřej Caletka
Licence: MIT
"""

import csv
import sys

def readcsv(filename):
    """
    Read provided CSV file. Yield each row as a dict.
    """
    with open(filename, newline='', encoding="iso-8859-2") as blf:
        yield from csv.DictReader(blf, delimiter=';')


def filter_active_domains(rows):
    """
    Read list of CSV rows as dicts.
    Yield domain names that have not been deleted from the list.
    """
    for row in rows:
        if row["Výmaz zveřejněných údajů IS"] == "":
            yield row["Adresa Internetové stránky"]


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: parse_csv.py <CSV file>")
    for name in filter_active_domains(readcsv(sys.argv[1])):
        print(name)


if __name__ == '__main__':
    main()
