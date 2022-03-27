from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView#create form automaticly using CreateView
from classapp import models
from django.urls import reverse_lazy#in delete view in order to use succes_url object
# Create your views here.
def index(request):
   return HttpResponse('hello')

class Indexview(View):
    def get(self,request):
        return HttpResponse('Hello my my')

class Templatesview(TemplateView):
    template_name='classapp/index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['text1']='ok'
        context['text2']='i am shihab'
        return context

class Listviews(ListView):#in listview we need not write any query
    context_object_name='list_of_musician'
    model=models.Musician
    template_name='classapp/listview.html'
class Musician_detail(DetailView):
    context_object_name='musician'
    model=models.Musician
    template_name='classapp/musician_detail.html'
class AddMusician(CreateView):
    fields=('first_name','last_name')
    model=models.Musician

class UpdateMusician(UpdateView):
    fields=('first_name','last_name')
    model=models.Musician

class DeletMusician(DeleteView):
    context_object_name='musician'#if u dont use the context object name it will send lower form of model name
    model=models.Musician
    success_url=reverse_lazy("classapp:listview")
    template_name='classapp/delete_musician.html'
