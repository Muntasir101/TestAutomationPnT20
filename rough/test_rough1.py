import pytest


@pytest.fixture
def main():
    print("Browser Launched")

    yield main
    print("Browser Close")


def test_TC_001(main):
    print("Test Case 1 executed.")


def test_TC_002(main):
    print("Test Case 2 executed.")
