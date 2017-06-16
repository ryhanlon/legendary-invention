from django.shortcuts import render
from .models import Sput

# Create your views here.


def create_sput(request):
    """
    Creates a single sput for a single user.

    """
    context = {}
    return render(request, '', context)


def read_sput(request, pk):
    """
    Reads a single sput.

    """
    sput = Sput.objects.get(id=pk)
    purr = "!@rty"
    context = {'sput': sput, 'purr': purr}
    return render(request, 'detail.html', context)


def update_sput(request):
    """
    Updates a single sput for a single user.

    """
    context = {}
    return render(request, '', context)


def delete_sput(request):
    """
    Deletes a single sput for a single user.

    """
    context = {}
    return render(request, '', context)


def list_sputs(request):
    """
    Returns a list for all sputts.

    """
    sputs = Sput.objects.all()
    context = {'sputs': sputs}
    return render(request, 'base.html', context)