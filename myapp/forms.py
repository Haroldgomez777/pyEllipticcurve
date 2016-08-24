# -*- coding: utf-8 -*-

from django import forms
from .models import Msg,Document



class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ('docfile',)

# DocumentFormset = inlineformset_factory(User,
#     fields = ('docfile',))

class MsgForm(forms.ModelForm):

    class Meta:
        model = Msg
        fields = ('user',)
