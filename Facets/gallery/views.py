from django.shortcuts import render, redirect
from .models import Media
from .forms import MediaModelForm
from django.contrib import messages



def create(request):
    """
    Create one media file entry.

    """
    # checking for which request verb:GET,
    if request.method == "GET":
        form = MediaModelForm()

    elif request.method == 'POST':
        form = MediaModelForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.INFO, 'Created!')
            return redirect('/gallery/display')

    context = {'form': form}
    return render(request, 'create.html', context)


def retrieve(request, pk):
    """
    Retrieve media from the data base.

    """

    media = Media.objects.get(id=pk)
    context = {'media': media}
    return render(request, 'detail.html', context)


def update(request, pk):
    """
    Update media in the data base.

    """
    media = Media.objects.get(id=pk)

    if request.method == "GET":
        form = MediaModelForm(instance=media)

    elif request.method == 'POST':
        form = MediaModelForm(instance=media, data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.INFO, 'Updated!')
            return redirect('/gallery/display')

    context = {'from': form}
    return render(request, 'create.html', context)


def delete(request, pk):
    """
    Delete media from the data base.

    """
    media = Media.objects.get(id=pk)
    message = {'status': f'Deleted {media.id}'}
    media.delete()

    context = {'status': message}

    return render(request, '', context)


def display(request, pk):
    """
    Display a list of all of the media from the data base.

    """
    context = {}
    return render(request, 'detail.html', context)
