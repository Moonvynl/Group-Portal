from calendar_events.models import Event
import datetime
import calendar

def next_date(date):
    day_count_next = calendar.monthrange(
        date.year if date.month < 12 else date.year + 1,
        date.month + 1 if date.month < 12 else 1
    )[1]

    return datetime.datetime(
        date.year if date.month < 12 else date.year + 1,
        date.month + 1 if date.month < 12 else 1,
        day_count_next if day_count_next < date.day else date.day
    )

def previous_date(date):
    day_count_previous = calendar.monthrange(
        date.year if date.month > 1 else date.year - 1,
        date.month - 1 if date.month > 1 else 12
    )[1]

    return datetime.datetime(
        date.year if date.month > 1 else date.year - 1,
        date.month - 1 if date.month > 1 else 12,
        day_count_previous if day_count_previous < date.day else date.day
    )

def selected_date_events(date):

    events = Event.objects.filter(
        scheduled_date__year=date.year,
        scheduled_date__month=date.month,
        scheduled_date__day=date.day
    ).all()

    return events

def month_events(date):

    month = Event.objects.filter(
        scheduled_date__year=date.year,
        scheduled_date__month=date.month
    ).all()

    return [event.scheduled_date.day for event in month]