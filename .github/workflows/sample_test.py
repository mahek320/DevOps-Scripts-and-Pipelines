import pytest
from app import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5  # ✅ Should pass

def test_add_numbers_fail():
    assert add_numbers(2, "3") == 5  # ❌ Should fail due to type mismatch

if __name__ == "__main__":
    pytest.main()
