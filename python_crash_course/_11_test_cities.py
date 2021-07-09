import unittest
from _11_example_function import get_formatted_location

class LocationsTestCase(unittest.TestCase):
	"""Test for '_11_city_functions.py'."""

	def test_city_country(self):
		"""Do locations like 'Carlisle, England' work?"""
		formatted_city = get_formatted_location('carlisle', 'England')
		self.assertEqual(formatted_city, 'Carlisle, England')

	def test_city_country_pop(self):
		formatted_city = get_formatted_location('santiago', 'chile', 50000000)
		self.assertEqual(formatted_city, 'Santiago, Chile - Population 50000000')

unittest.main()