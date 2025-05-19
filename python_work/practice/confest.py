import pytest


@pytest.fixture(scope="class")
def setup():
    lis_words = input("Enter the words sentence ").split(" ")
