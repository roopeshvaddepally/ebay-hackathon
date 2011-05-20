from django.http import HttpResponse

def index(request):
    if request.method == "GET":
        # call get method
        do_get(request)
    elif request.method == "POST":
        # call post method
        do_post(request)


def do_get(request):
    query_type = request.GET["type"]
    print query_type


    

