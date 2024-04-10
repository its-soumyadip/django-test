# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime
# create a function
def home(request):
# fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Hello Soumyadip. "
    html += " Time is {}".format(now)
    return HttpResponse(html)
# return response