from django.shortcuts import render, redirect

from Body.models import Post


# Create your views here.

def main(request):

    post = Post.objects.all()

    return render(request, 'front/main.html')

# def main(request):
#
#     return render(request, 'front/main.html')