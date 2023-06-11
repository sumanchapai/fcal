#!/usr/bin/env python

import argparse
import datetime 
import sys


def display(
        start: datetime.datetime, 
        end:datetime.datetime, 
        fmt: str,
        increment : datetime.timedelta = datetime.timedelta(days=1)
        ):
    """"
    Prints to stdout the date from `start` to `end` in specified format
    """
    while start < end:
        sys.stdout.write(start.strftime(fmt))
        start += increment


def main():
    parser = argparse.ArgumentParser()
    # Days before current day
    parser.add_argument("-b", "--before", metavar='', type=int, default=1)
    # Days after current day
    parser.add_argument("-a", "--after", metavar='', type=int, default=1)
    # Display format
    parser.add_argument("-f", "--format", metavar='', type=str,
            default="%y-%m-%d\n") # Locale
    args = parser.parse_args()
    now = datetime.datetime.now()
    start_date = now - datetime.timedelta(days=args.before)
    end_date = now + datetime.timedelta(days=args.after)
    if not args.format.startswith('%'):
        args.format = '%' + args.format
    display(start_date, end_date, args.format)


if __name__ == "__main__":
    main()