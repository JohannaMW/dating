from django.shortcuts import render, render_to_response, redirect, HttpResponse
from django.template import RequestContext
# from date.models import Single, Preference
# from date.forms import EmailUserCreationForm, CoreBeliefsForm, ArguesForm
# from date.forms import BreakupForm, RelationKindForm, RelationLastForm,RightPersonForm, RomanceForm, StatusForm, PreferenceForm
# from django.core import serializers
# from django.views.decorators.csrf import csrf_exempt
# import json
from date.forms import SingleForm, EmailUserCreationForm, PreferenceForm

def home(request):
    return render_to_response("home.html", {},
                          context_instance=RequestContext(request))

def profile(request):
    return render_to_response("profile.html", {},
                          context_instance=RequestContext(request))

def questions(request):
    return render_to_response("questions.html", {},
                          context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("questionnaire")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def questions(request):
    if request.method == 'POST':
        form = SingleForm(request.POST)
        if form.is_valid():
             if form.save():
                return redirect("/preferences/")
    else:
        form = SingleForm()
    data = {"form": form}
    return render(request, "questions.html", data)

def preferences(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
             if form.save():
                return redirect("/profile/")
    else:
        form = PreferenceForm()
    data = {"form": form}
    return render(request, "preferences.html", data)
