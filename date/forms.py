__author__ = 'johanna'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from date.models import Single, Preference
from django.forms import ModelForm

class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Single
        fields = ("username", "email", "password1", "password2")

class SingleForm(ModelForm):
    class Meta:
        model = Single
        fields = ("first_name", "last_name", "location", "paid", "age", "image", "gender")

class PreferenceForm(ModelForm):
    class Meta:
        model = Preference


# class StatusForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['status']
#
# class BreakupForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['breakup']
#
# class RomanceForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['romance']
#
# class ArguesForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['argues']
#
# class RelationKindForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['relation_kind']
#
#
# class RelationLastForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['relation_last']
#
# class CoreBeliefsForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['core_beliefs']
#
# class RightPersonForm(ModelForm):
#     class Meta:
#         model = Preference
#         fields = ['right_person']
