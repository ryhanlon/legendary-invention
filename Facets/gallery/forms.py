"""
Forms for Update and Delete of Media Records.

"""

from django import forms
from .models import Media


# Write your forms here.

class MediaModelForm(forms.ModelForm):
    """
    A model form for manipulating Media records.

    """

    class Meta:
        model = Media
        fields = ('name', 'type', 'file',
                  'is_published', 'tags')


