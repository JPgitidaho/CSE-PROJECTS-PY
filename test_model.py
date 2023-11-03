import pytest
import pandas as pd
import re

from verify_news import preprocess_text, is_reliable_source, verify_article

# Tests for the preprocess_text function
def test_preprocess_text():
    text = "This is a Test!"
    expected_output = "this is a test"
    assert preprocess_text(text) == expected_output

# Tests for the is_reliable_source function
def test_is_reliable_source():
    assert is_reliable_source("CNN") == True
    assert is_reliable_source("Fake News") == False



if __name__ == '__main__':
    pytest.main()
