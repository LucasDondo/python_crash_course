import unittest
from city_functions import formatted_city


class CitiesTestCase(unittest.TestCase):
    ''' Tests for "city_functions.py". '''

    def test_city_country(self):
        ''' Is the formatted name correct? '''

        formatted = formatted_city('buenos aires', 'argentina')
        self.assertEqual(formatted, 'Buenos Aires, Argentina.')

    def test_city_country_population(self):
        ''' Does the formatted population work? '''

        formatted = formatted_city(
            'buenos aires', 'argentina', population=5_000_000)
        self.assertEqual(
            formatted, 'Buenos Aires, Argentina.\nPopulation: 5000000.')


if __name__ == '__main__':
    unittest.main()
