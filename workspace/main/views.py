from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return render(request, 'homepage.html', locals())
