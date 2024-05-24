from city_function import cityCountry
import unittest





class CityTest(unittest.TestCase):
        def test_city_country(self):
            self.assertEqual(cityCountry("santiago", "chile"), "santiago, chile")

if __name__ == '__main__':
    unittest.main()