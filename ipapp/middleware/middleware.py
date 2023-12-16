import pytz
import requests
from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Assume you have a function to get the user's timezone from their IP address
        user_timezone = self.get_user_timezone(request.META.get('REMOTE_ADDR'))

        # Set the timezone in the request
        request.timezone = user_timezone or timezone.get_current_timezone()

        response = self.get_response(request)
        return response

    @staticmethod
    def get_user_timezone(ip_address):
        try:
            # Use ipinfo.io to get location information based on IP address
            response = requests.get(f'https://ipinfo.io/{ip_address}/json')
            data = response.json()

            # Extract the timezone from the response
            timezone_str = data.get('timezone')

            # Return a pytz timezone object
            return pytz.timezone(timezone_str) if timezone_str else None
        except Exception as e:
            # Log the error or handle it appropriately
            print(f"Error getting timezone for IP {ip_address}: {e}")
            return None  # Default to None if timezone detection fails
