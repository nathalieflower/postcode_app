import unittest

from main import get_postcode_info, get_nearest_postcodes, main, validate_postcode


class IsPostcodeValid(unittest.TestCase):
    def test_valid_postcode(self):
        postcode = "CB4 0GF"

        result = validate_postcode(postcode)

        self.assertTrue(result)

    def test_invalid_postcode(self):
        postcode = "Invalid Postcode"

        result = validate_postcode(postcode)

        self.assertFalse(result)


class PostCodeInfoReturnsCorrectPostcodeInfo(unittest.TestCase):
    def test_postcode_info(self):
        postcode = "CB4 0GF"
        region = "East of England"
        country = "England"

        result = get_postcode_info(postcode)

        self.assertNotEqual(result, None)
        self.assertEqual(result.region, region)
        self.assertEqual(result.country, country)


class NearestPostcodeReturnsCorrectNearestPostcodes(unittest.TestCase):
    def test_nearest_postcodes(self):
        postcode = "CB4 0GF"
        nearest_postcode_1 = "CB4 0GA"

        result = get_nearest_postcodes(postcode)

        postcode_1_count = sum(1 for item in result if item.postcode == nearest_postcode_1)

        self.assertEqual(postcode_1_count, 1)
        self.assertNotEqual(result, None)


if __name__ == '__main__':
    unittest.main()
