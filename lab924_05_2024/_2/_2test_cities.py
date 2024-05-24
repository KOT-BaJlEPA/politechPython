from _2city_function import _2cityCountry
import unittest





class CityTest2(unittest.TestCase):
        def test_city_country(self):
            self.assertEqual(_2cityCountry("Santiago", "Chile"), "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()