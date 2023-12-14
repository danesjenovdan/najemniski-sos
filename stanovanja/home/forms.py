from django import forms
import requests
import json
from .models.solution import RentalStory, UserProblem


class RentalStoryForm(forms.ModelForm):
    # newsletter = forms.BooleanField(required=False)

    class Meta:
        model = RentalStory
        fields = [
            "type_of_story",
            "description",
            "icon",
            "name",
            # "email",
            "address",
            "private",
            "hide_location",
        ]
        widgets = {
            "type_of_story": forms.RadioSelect(attrs={"required": True}),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control",
                    "placeholder": "Tvoja izkušnja*",
                }
            ),
            "icon": forms.TextInput(),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ime"}
            ),
            # "email": forms.TextInput(
            #     attrs={"class": "form-control", "placeholder": "E-naslov*"}
            # ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ulica in hišna številka, poštna številka in pošta*",
                }
            ),
            "private": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "hide_location": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def save(self, commit=True):
        # subscribe user to newsletter, if they said so in the form
        # send_emails = self.cleaned_data["newsletter"]
        # if send_emails:
        #     user_email = self.cleaned_data["email"]
        #     headers = {
        #         "Content-Type": "application/json",
        #     }
        #     payload = {
        #         "email": user_email,
        #         "segment": 20,
        #     }

        #     r = requests.post(
        #         "https://podpri.djnd.si/api/subscribe/",
        #         data=json.dumps(payload),
        #         headers=headers,
        #     )
        return super(RentalStoryForm, self).save(commit=commit)


class UserProblemSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserProblem
        fields = ["description", "email", "contact_permission"]
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control",
                    "placeholder": "Tvoje sporočilo*",
                }
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "E-naslov*"}
            ),
            "contact_permission": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }
