import pytest


@pytest.mark.cmoke
def test_smoke_case():
    assert 1 + 1 == 2



@pytest.mark.regression
def test_regression_case():
    assert 2 + 2 == 4


@pytest.mark.fast
def test_fast():
    assert 3 + 3 == 6