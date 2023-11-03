# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
Verify that the make_full_name, extract_family_name,
and extract_given_name functions work correctly.
"""

from names import make_full_name, \
     extract_family_name, extract_given_name
import pytest


def test_make_full_name(): 
    """Verify that the make_full_name function works properly."""
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Sally-Joe-Brown", "Brown") == "Brown; Sally-Joe-Brown"
    assert make_full_name("Lee", "Chu") == "Chu; Lee"
    assert make_full_name("T.", "Perry") == "Perry; T."
    assert make_full_name("", "") == "; "



def test_extract_family_name(): 
    """Verifies that the extract_family_name function works properly."""
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Brown; Sally-Joe-Brown") == "Brown"
    assert extract_family_name("Chu; Lee") == "Chu"
    assert extract_family_name("Perry; T.") == "Perry"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    """Verifies that the extract_given_name function works properly."""
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Brown; Sally-Joe-Brown") == "Sally-Joe-Brown"
    assert extract_given_name("Chu; Lee") == "Lee"
    assert extract_given_name("; ") == ""

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
