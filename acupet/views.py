from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from .models import Client
from .models import Pet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Creat

# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name = 'acupet/index.html'
    context_object_name = 'latest_client_list'

    def get_queryset(self):
        #return the clients List
        return Client.objects.order_by('client_name')

class DetailView(generic.DetailView):
    model = Client
    template_name = 'acupet/detail.html'

#view for testing custom tags
def articles_view(request):
    # return response
    return render(request, "myArticles.html")
