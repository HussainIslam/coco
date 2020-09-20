from django.shortcuts import render

def HomePageView(request):
    return render(request, 'home.html')

def MarkdownTutorialPageView(request):
    return render(request, 'markdown_tutorial.html')