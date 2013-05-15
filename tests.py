import unittest
from datetime import datetime, timedelta, date
import oxford_term_dates


class TestOxfordTermDates(unittest.TestCase):

    def test_first_day_term(self):
        defined = datetime(2012, 01, 8)
        dico = oxford_term_dates.ox_date_dict(defined)
        self.assertEqual(dico.get('term_short'), 'H')
        self.assertEqual(dico.get('term_long'), 'Hilary')
        self.assertEqual(dico.get('term'), 1)

    def test_normal_to_ox(self):
        defined = datetime(2012, 01, 19)
        year, term, week, day = oxford_term_dates.normal_to_ox(defined.date())
        self.assertEqual(year, 2012)
        self.assertEqual(term, 1)
        self.assertEqual(week, 1)
        self.assertEqual(day, 4)

    def test_ox_to_normal(self):
        defined = date(2012, 01, 19)
        normal = oxford_term_dates.ox_to_normal(2012, 1, 1, 4)
        self.assertEqual(defined, normal)

    def test_term_start(self):
        defined = date(2012, 01, 8)
        result = oxford_term_dates.term_start(defined)
        self.assertEqual((2012, 1), result)

    def test_term_as_string(self):
        term = oxford_term_dates.term_as_string(2012, 1)
        self.assertEqual("20121", term)

    def test_format(self):
        dico = oxford_term_dates.ox_date_dict(datetime(2013, 05, 14))
        formatted = oxford_term_dates.format_date(dico)
        self.assertEqual("Tuesday, 4th week, Trinity 2013 (14 May)", formatted)

if __name__ == "__main__":
    unittest.main()
