#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a function that returns today's date and also conditionally executes
that date if it's run on the command line"""


import datetime
CURDATE = None

def get_current_date():
    """This function returns today's date and also conditionally executes
    that date if it's not in the command line

    Args:
        CURDATE(str): Current date

    Returns:
        datetime.date.today(): Returns today's date

    Examples:
    >>> import task_01
    >>> print task_01.CURDATE
    None
    >>> task_01.get_current_date()
    datetime.date(2016, 9, 21)

    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
