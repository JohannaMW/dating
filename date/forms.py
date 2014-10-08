__author__ = 'johanna'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from date.models import Single
from django.forms import ModelForm


class SingleForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Single
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Single.objects.get(username=username)
        except Single.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

class SingleDataForm(ModelForm):
    class Meta:
        model = Single
        fields = ("location", "paid", "age", "image", "gender", "status")


class PreferenceForm(ModelForm):
    class Meta:
        model = Single
        fields = ("breakup", "romance", "argues", "relation_kind", "relation_last", "core_beliefs", "right_person")



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
