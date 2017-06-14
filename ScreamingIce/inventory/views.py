from django.shortcuts import render
from .models import IceCream

# Create your views here.

def scream_maker(request):
    """
    Creates a new ice cream record in the database from the user's submitted form data.

    A view is a function that takes an HTTP REQUEST and returns AN HTTP RESPONSE.

    """
    pass
    return render(request, 'index.html')


def scream_taker(request, pk):
    """
    Retrieve a new ice cream record in the database from the url.

    """
    icecream = IceCream.objects.get(pk=pk)
    context = {'scream': icecream}
    return render(request, context)