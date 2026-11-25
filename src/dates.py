def add_days(year: int, day_of_year: int) -> tuple[int, int]:
    """Naive helper: adding one day at year end must roll into next year."""
    if day_of_year > 365:
        return year + 1, 1
    return year, day_of_year + 1
