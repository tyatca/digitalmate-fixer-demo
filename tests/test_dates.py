from src.dates import add_days


def test_normal_day():
    assert add_days(2026, 100) == (2026, 101)


def test_year_boundary():
    assert add_days(2026, 365) == (2027, 1)
