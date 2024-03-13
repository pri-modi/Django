from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello");

def removePunc(request):
    return HttpResponse("Remove Punctuation");

def capitalizeFirst(request):
    return HttpResponse("Capitalize First");

def newLinerRemove(request):
    return HttpResponse("New Line Remover");

def spaceRemove(request):
    return HttpResponse("Space Remover");

def charCount(request):
    return HttpResponse("Character Count");
