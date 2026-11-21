"""
Demonstrates usage of the datetime module.
"""

from datetime import datetime, date, time, timedelta


def get_current_datetime() -> datetime:
    """Return the current local date and time as a datetime object."""
    return datetime.now()


def get_current_date() -> date:
    """Return the current local date as a date object."""
    return date.today()


def get_current_time() -> time:
    """Return the current local time as a time object."""
    return datetime.now().time()


def add_days_to_date(days: int) -> date:
    """Return a new date that is `days` days after today."""
    return date.today() + timedelta(days=days)


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime object into a string using the given format."""
    return dt.strftime(fmt)


def main() -> None:
    now = get_current_datetime()
    print(f"Current datetime: {now}")
    print(f"Current date: {get_current_date()}")
    print(f"Current time: {get_current_time()}")
    print(f"Date 5 days from now: {add_days_to_date(5)}")
    print(
        f"Formatted datetime: {format_datetime(now, '%A, %B %d, %Y %I:%M %p')}"
    )


if __name__ == "__main__":
    main()