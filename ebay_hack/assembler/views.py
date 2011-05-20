from django.http import HttpResponse
from django.shortcuts import render_to_response
from ebay_hack.api_wrapper.calls import findItemsByKeywords as find
from json import loads


def index(request):
    if request.method == "GET":
        # call get method
        #return HttpResponse("hello")
        return do_get(request)
    elif request.method == "POST":
        # call post method
        return do_post(request)

def do_get(request):
    if request.GET:
        # subsequent calls for functions based on parameter
        if request.GET["type"] == "ram":
            return get_ram_list(request)
        elif request.GET["type"] == "hdd":
            return get_hdd_list(request)
        elif request.GET["type"] == "monitor":
            return get_monitor_list(request)
        elif request.GET["type"] == "keyboard":
            return get_keyboard_list(request)
        elif request.GET["type"] == "mouse":
            return get_mouse_list(request)
        elif request.GET["type"] == "motherboard":
            return get_motherboard_list(request)
        elif request.GET["type"] == "processor":
            return get_processor_list(request)
        elif request.GET["type"] == "case":
            return get_case_list(request)
        elif request.GET["type"] == "video":
            return get_video_list(request)
        elif request.GET["type"] == "drive":
            return get_drive_list(request)
        else:
            return render_to_response("index.html", {"p": request.GET})
    else:
        return render_to_response("index.html", {"p": request.GET})


    
def get_ram_list(request):
    # call the api for searching ram
    return get_search_results(request.GET["value"])

def get_hdd_list(request):
    return get_search_results(request.GET["value"]+" hard drive")

def get_monitor_list(request):
    return get_search_results(request.GET["value"]+" desktop monitor")

def get_keyboard_list(request):
    return get_search_results(request.GET["value"]+" computer keyboard")

def get_mouse_list(request):
    return get_search_results(request.GET["value"]+" mouse")

def get_motherboard_list(request):
    return get_search_results(request.GET["value"]+" motherboard")

def get_processor_list(request):
    return get_search_results(request.GET["value"]+" processor")

def get_case_list(request):
    return get_search_results(request.GET["value"]+" desktop cabinet")

def get_video_list(request):
    return get_search_results(request.GET["value"])

def get_drive_list(request):
    return get_search_results(request.GET["value"])


def get_search_results(search_key)
    response = find(search_key)
    a = loads(response)
    result = []
    try:
        b = a["findItemsByKeywordsResponse"][0]["searchResult"][0]
        result = [(each['itemId'][0], each['title'][0], each['location'][0]) for each in b['item']]
    except: pass
    return render_to_response("index.html",{"result": result})


def get_404_error(request):
    return render_to_response("index.html",{"p": "keyboard_list"})

    


