from django import forms
from .models.solution import RentalStory, UserProblem


class RentalStoryForm(forms.ModelForm):
    class Meta:
        model = RentalStory
        fields = ['description', 'icon', 'name', 'email', 'address', 'private']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': "form-control", 'placeholder': 'Tvoja izkušnja'}),
            'icon': forms.TextInput(),
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Ime'}),
            'email': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'E-naslov'}),
            'address': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Ulica , poštna številka in pošta'}),
            'private': forms.CheckboxInput(attrs={'class': "form-check-input"})
        }


class UserProblemSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserProblem
        fields = ['description', 'email', 'contact_permission']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': "form-control", 'placeholder': 'Tvoja dilema'}),
            'email': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'E-naslov'}),
            'contact_permission': forms.CheckboxInput(attrs={'class': "form-check-input"})
        }
