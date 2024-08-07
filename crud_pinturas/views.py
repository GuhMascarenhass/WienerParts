from django.shortcuts import render


def test(request):
    return render(request, "crud_pinturas\index.html")


# Create your views here.
