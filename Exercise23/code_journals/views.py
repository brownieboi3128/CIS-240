from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for code_journals."""
    return render(request, 'code_journals/index.html')