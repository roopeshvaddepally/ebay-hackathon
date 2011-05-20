from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    if request.method == "GET":
        # call get method
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
            return get get_404_error(request)
    else:
        return render_to_response("index.html", {"p": request.GET})


    
def get_ram_list(request):
    # call the api for searching ram
    return render_to_response("index.html",{"p": "ram list"})

def get_hdd_list(request):
    return render_to_response("index.html",{"p": "hdd list"})

def get_monitor_list(request):
    return render_to_response("index.html",{"p": "monitor_list"})

def get_keyboard_list(request):
    return render_to_response("index.html",{"p": "keyboard_list"})




    

>>>>>>> 4334a58ff0102f562fd82919f0cf3dc6f5847fa4
