from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def counter(request):
    text_file = open("./templates/countej.html", "r")
    page = text_file.read()
    text_file.close()
    return HttpResponse(page)
def basic(request):
    text_file = open("./templates/countej.html", "r")
    page = text_file.read()
    text_file.close()