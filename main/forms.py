from django import forms

from main.models import Item

input_class = 'form-control'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {

            'category': forms.Select(attrs={
                'class': input_class
            }),

            'name': forms.TextInput(attrs={
                'class': input_class
            }),

            'description': forms.Textarea(attrs={
                'class': input_class
            }),

            'price': forms.TextInput(attrs={
                'class': input_class
            }),

            'image': forms.FileInput(attrs={
                'class': input_class
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image')
        widgets = {

            'name': forms.TextInput(attrs={
                'class': input_class
            }),

            'description': forms.Textarea(attrs={
                'class': input_class
            }),

            'price': forms.TextInput(attrs={
                'class': input_class
            }),

            'image': forms.FileInput(attrs={
                'class': input_class
            })
        }
