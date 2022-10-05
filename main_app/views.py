from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Finch, Picture, Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context

class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}..."
        else:
            context["finches"] = Finch.objects.all()
            context["header"] = "Trending Finches"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'bio']
    template_name = "finch_create.html"
    success_url = "/finches"

class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context
        
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'bio']
    template_name = "finch_update.html"
    success_url = "/finches"

class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete_confirmation.html"
    success_url = "/finches"

class PictureCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        url = request.POST.get("url")
        finch = Finch.objects.get(pk=pk)
        Picture.objects.create(title=title, url=url, finch=finch)
        return redirect('finch_detail', pk=pk)

class AlbumPictureAssoc(View):

    def get(self, request, pk, picture_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Album.objects.get(pk=pk).pictures.remove(picture_pk)
        if assoc == "add":
            Album.objects.get(pk=pk).pictures.add(picture_pk)
        return redirect('home')