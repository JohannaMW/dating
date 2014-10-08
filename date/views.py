from django.shortcuts import render, render_to_response, redirect, HttpResponse
from django.template import RequestContext
from date.models import Single
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
# from date.models import Single, Preference
# from date.forms import EmailUserCreationForm, CoreBeliefsForm, ArguesForm
# from date.forms import BreakupForm, RelationKindForm, RelationLastForm,RightPersonForm, RomanceForm, StatusForm, PreferenceForm
# from django.core import serializers
# from django.views.decorators.csrf import csrf_exempt
# import json
from date.forms import SingleForm, PreferenceForm, SingleDataForm
import braintree
from django.db.models import Q

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    'rk3dxfj47wbkb6sv',
    '2rnwqh8fxqp94qyz',
    '6b5706a60389167d66ce46452c8ca95c'
)

def home(request):
    return render_to_response("home.html", {},
                          context_instance=RequestContext(request))

def profile(request):
    return render_to_response("profile.html", {},
                          context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = SingleForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("data")
    else:
        form = SingleForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def data(request):
    single = Single.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = SingleDataForm(request.POST, instance=single)
        if form.is_valid():
             if form.save():
                return redirect("questions")
    else:
        form = SingleDataForm()
    data = {"form": form}
    return render(request, "questions.html", data)

def questions(request):
    single = Single.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = PreferenceForm(request.POST, instance=single)
        if form.is_valid():
             if form.save():
                return redirect("/profile/")
    else:
        form = PreferenceForm()
    data = {"form": form}
    return render(request, "questions.html", data)

def payment_error(request):
    return render_to_response("payment_error.html", {},
                          context_instance=RequestContext(request))

def confirmation(request):
    return render_to_response("confirmation.html", {},
                          context_instance=RequestContext(request))

def form(request):
    return render_to_response("braintree.html", {},
                          context_instance=RequestContext(request))

def create_transaction(request):
        result = braintree.Transaction.sale({
            "amount": "30.00",
            "credit_card": {
                "number":  "4111111111111111",
                "cvv":  "111",
                "expiration_month": request.POST["month"],
                "expiration_year": request.POST["year"]
            },
            "options": {
                "submit_for_settlement": True
            }
        })
        if result.is_success:
            Single.objects.filter(username=request.user.username).update(paid=True)
            return redirect("/confirmation/")
        else:
            return redirect("/payment_error/")

@csrf_exempt
def search_singles(request, search_query):
    results = Single.objects.filter(Q(first_name__icontains=search_query) |
                                Q(last_name__icontains=search_query) | Q(age__icontains=search_query)|
                                Q(gender__icontains=search_query) | Q(name__icontains=search_query) |
                                Q(username__icontains=search_query) ).order_by('name')
    return render(request, 'search_result.html', {"results" : results})

def singles(request):
    return render_to_response("singles.html", {},
                          context_instance=RequestContext(request))

def single_profile(request, single_id):
    single = Single.objects.get(id=single_id)
    return render(request, "single_profile.html", {"single" : single})



