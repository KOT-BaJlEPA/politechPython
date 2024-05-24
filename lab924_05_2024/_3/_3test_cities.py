from _3city_function import _3cityCountry
import unittest





class CityTest3(unittest.TestCase):
        def test_city_country(self):
            self.assertEqual(_3cityCountry("Santiago", "Chile", 5000000), "Santiago, Chile - population 5000000.")

if __name__ == '__main__':
    unittest.main()