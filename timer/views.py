from django.shortcuts import render
from .models import Event
from datetime import datetime
from django.utils import timezone


def countdown_timer(request):
    # Retrieve the first event from the database (you can customize this logic)
    event = Event.objects.first()

    # Assume you have an offset-naive datetime (e.g., from a form submission)
    naive_datetime = datetime(2024, 3, 8, 10, 30)
    # Convert it to an offset-aware datetime using the default timezone (settings.TIME_ZONE)
    aware_datetime = timezone.make_aware(naive_datetime)
    time_remaining = event.event_date - aware_datetime

    # Extract hours, minutes, and seconds from the time_remaining
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Prepare data to pass to the template
    data = {
        'name': event.name,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }
    return render(request, 'myapp/index.html', {'data': data})

