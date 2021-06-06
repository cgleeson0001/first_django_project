from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(data = {

   "Name" : "Chantel Gleeson",

    "Track" : "Backend(Python)",

    "Message" : "Hello Everyone"

}

)