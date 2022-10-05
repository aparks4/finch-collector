from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from .models import Finch, Picture, Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}..."
        else:
            context["finches"] = Finch.objects.filter(user=self.request.user)
            context["header"] = "Trending Finches"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'bio']
    template_name = "finch_create.html"
    success_url = "/finches"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FinchCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

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

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)