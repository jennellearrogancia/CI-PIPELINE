import pytest
from age import is_adult


class TestAgeChecker(pytest.TestCase):

    def test_adult(self):
        self.assertTrue(is_adult(20))

    def test_not_adult(self):
        self.assertFalse(is_adult(17))

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            is_adult(-5)

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            is_adult("twenty")

        with self.assertRaises(ValueError):
            is_adult(18.5)


if __name__ == "__main__":
    pytest.main()
