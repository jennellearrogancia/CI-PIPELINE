import pytest
from age import is_adult


class TestAgeChecker:

    def test_adult(self):
        assert is_adult(18) is True

    def test_not_adult(self):
        assert is_adult(17) is False

    def test_negative_age(self):
        with pytest.raises(ValueError):
            is_adult(-5)

    def test_non_integer_input(self):
        with pytest.raises(ValueError):
            is_adult("eighteen")

        with pytest.raises(ValueError):
            is_adult(17.5)


if __name__ == "__main__":
    pytest.main()
