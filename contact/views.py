from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import FeedBackForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    form = FeedBackForm()
    context = {"form": form}
    return render(request, "contact.html", context)


def thanks(request):
    return render(request, "thanks.html")
