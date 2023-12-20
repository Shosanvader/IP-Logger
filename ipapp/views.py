from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserIP
import pytz
import zoneinfo

#This function defines the view for homepage
def home(request):
    return render(request, 'home.html')

"""This function collects the IP address and stores in the database.
    It also displays the current IP address"""
def current_ip(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')

    # Save the IP address to the database
    UserIP.objects.create(ip_address=user_ip)

    # Convert UTC timestamp to the user's local timezone
    utc_timestamp = UserIP.objects.latest('timestamp').timestamp
    local_time = convert_utc_to_local(utc_timestamp, request.timezone)


    return render(request, 'current_ip.html', {'current_ip': user_ip, 'local_time': local_time})


def convert_utc_to_local(utc_timestamp, user_timezone):
    # Ensure that utc_timestamp is a naive datetime object
    utc_time_naive = utc_timestamp.replace(tzinfo=None)

    # Convert to the user's local timezone
    local_time_naive = utc_time_naive.astimezone(user_timezone)

    # Reapply the user's local timezone information to the naive datetime
    local_time = datetime.combine(local_time_naive.date(), local_time_naive.time(), tzinfo=user_timezone)

    return local_time

# This function displays all the logged IP addresses.
def view_logged_ips(request):
    logged_ips = UserIP.objects.all()
    return render(request, 'view_logged_ips.html', {'logged_ips': logged_ips})