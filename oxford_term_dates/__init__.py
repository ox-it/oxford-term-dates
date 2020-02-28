from datetime import date, datetime, timedelta

# Requirements:
# * Convert from an ox date to a normal date                ox_to_normal
# * Convert from a normal date to an ox date                normal_to_ox
# * Find the most recent start-of-term for a given date     term_start
# * Convert a (year, term) pair to a string                 term_as_string
# * Convert a string to a (year, term) pair                 term_from_string
# * Prettyprint a (year, term) pair                         get_term_display

TERM_NAMES = {
    1: 'Hilary',
    2: 'Trinity',
    3: 'Michaelmas',
}

TERM_NAMES_INV = {
    'h': 1, 'Hilary': 1,
    't': 2, 'Trinity': 2,
    'm': 3, 'Michaelmas': 3,
}

TERM_LETTERS = {
    1: 'h',
    2: 't',
    3: 'm',
}

# from http://www.ox.ac.uk/about_the_university/university_year/dates_of_term.html
# take the date from the main website, remove 7 days
TERM_STARTS = {
    (2007, 3): date(2007,  9, 30),
    (2008, 1): date(2008,  1,  6),
    (2008, 2): date(2008,  4, 13),
    (2008, 3): date(2008, 10,  5),
    (2009, 1): date(2009,  1, 11),
    (2009, 2): date(2009,  4, 19),
    (2009, 3): date(2009, 10,  4),
    (2010, 1): date(2010,  1, 10),
    (2010, 2): date(2010,  4, 18),
    (2010, 3): date(2010, 10,  3),
    (2011, 1): date(2011,  1,  9),
    (2011, 2): date(2011,  4, 24),
    (2011, 3): date(2011, 10,  2),
    (2012, 1): date(2012,  1,  8),
    (2012, 2): date(2012,  4, 15),
    (2012, 3): date(2012, 9, 30),
    (2013, 1): date(2013, 1, 6),
    (2013, 2): date(2013, 4, 14),
    (2013, 3): date(2013, 10, 6),
    (2014, 1): date(2014, 1, 12),
    (2014, 2): date(2014, 4, 20),  # Easter Sunday?
    (2014, 3): date(2014, 10, 5),
    (2015, 1): date(2015, 1, 11),
    (2015, 2): date(2015, 4, 19),
    (2015, 3): date(2015, 10, 4),
    (2016, 1): date(2016, 1, 10),
    (2016, 2): date(2016, 4, 17),
    (2016, 3): date(2016, 10, 2),
    (2017, 1): date(2017, 1, 8),
    (2017, 2): date(2017, 4, 16),
    (2017, 3): date(2017, 10, 1),
    (2018, 1): date(2018, 1, 7),
    (2018, 2): date(2018, 4, 15),
    (2018, 3): date(2018, 9, 30),
    (2019, 1): date(2019, 1, 6),
    (2019, 2): date(2019, 4, 21),
    (2019, 3): date(2019, 10, 6),
    (2020, 1): date(2020, 1, 12),
    (2020, 2): date(2020, 4, 19),
    (2020, 3): date(2020, 10, 4),
    (2021, 1): date(2021, 1, 10),
    (2021, 2): date(2021, 4, 18),
    # Provisional from here onwards
    (2021, 3): date(2021, 10, 3),
    (2022, 1): date(2022, 1, 9),
    (2022, 2): date(2022, 4, 17),
    (2022, 3): date(2022, 10, 2),
    (2023, 1): date(2023, 1, 8),
    (2023, 2): date(2023, 4, 16),
    (2023, 3): date(2023, 10, 1),
    (2024, 1): date(2024, 1, 7),
    (2024, 2): date(2024, 4, 14),
    (2024, 3): date(2024, 10, 6),
    (2025, 1): date(2025, 1, 12),
    (2025, 2): date(2025, 4, 20),
}

# Sanity check; all dates should be Sundays
assert all(dt.isoweekday() == 7 for dt in TERM_STARTS.values())

OFFSET_TERM_STARTS = dict((k, v-timedelta(14)) for k, v in TERM_STARTS.items())

DAY_NAMES = [
    'Sunday', 'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday'
]

TERM_STARTS_LIST = sorted(TERM_STARTS.items())
OFFSET_TERM_STARTS_LIST = sorted(OFFSET_TERM_STARTS.items())


def get_term_display(s):
    return "%s %s" % (TERM_NAMES[int(s[4])], s[:4])


def term_as_string(year=None, term=None):
    if year is None:
        year, term = term_start()
    return "%d%d" % (year, term)


def term_start(pdate=None):
    if pdate is None:
        pdate = date.today()
    for i in range(1, len(OFFSET_TERM_STARTS_LIST)):
        if OFFSET_TERM_STARTS_LIST[i-1][1] <= pdate and OFFSET_TERM_STARTS_LIST[i][1] > pdate:
            break
    return OFFSET_TERM_STARTS_LIST[i-1][0]


def ox_to_normal(year, term, week=0, day=0):
    return TERM_STARTS[(year, term)] + timedelta(week*7+day)


def normal_to_ox(pdate):
    year, term = term_start(pdate)
    week, day = divmod((pdate - OFFSET_TERM_STARTS[(year, term)] - timedelta(14)).days, 7)
    return (year, term, week, day)


def ox_date_dict(dt=None):
    if dt is None:
        dt = date.today()
    elif isinstance(dt, datetime):
        dt = dt.date()
    year, term, week, day = normal_to_ox(dt)
    return {
        'day_name': DAY_NAMES[day],
        'day_name_short': DAY_NAMES[day][:3],
        'day': day,
        'week': week,
        'ordinal': 'th' if 10 < week < 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(abs(week) % 10, 'th'),
        'term': term,
        'term_short': TERM_LETTERS[term].upper(),
        'term_long': TERM_NAMES[term],
        'year': year,
        'day_number': dt.day,
        'month': dt.strftime('%b'),
        'month_long': dt.strftime('%B'),
    }


def format_date(date_dict):
    """Format a date to "standard" Oxford format
    :param date_dict: date dict
    :return: String
    """
    return "%(day_name)s, %(week)d%(ordinal)s week, %(term_long)s %(year)d (%(day_number)d %(month)s)" % date_dict

def format_date_nocal(date_dict):
    """Format a date to "standard" Oxford format, but excluding the calendar date at the end
    :param date_dict: date dict
    :return: String
    """
    return "%(day_name)s, %(week)d%(ordinal)s week, %(term_long)s %(year)d" % date_dict

def format_today():
    return format_date(ox_date_dict())
