from django.shortcuts import render
# Create your views here.

def main(request):
    return render(request, 'front/main.html')

# def main(request):
#
#     return render(request, 'front/main.html')