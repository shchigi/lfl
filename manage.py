#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lfl.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    from plays.add_test_data import add_test_data
    print "Adding test data to database ..."
    add_test_data()
