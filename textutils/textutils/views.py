# Created by self
from django.http import HttpResponse

# Pass the parameter 'request'
def index(request):
    return HttpResponse('''<h1>Hello!</h1> <a href="https://www.youtube.com/">Youtube </a>,
    <a href="https://www.w3schools.com/"> W3Schools </a>''')

def about(request):
    return HttpResponse("Hello World")

def w3schools(request):
    return HttpResponse('''<a href="https://www.w3schools.com/"> W3Schools </a>''')