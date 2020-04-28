# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView
from django.shortcuts import redirect
from .models import Pictures
from .forms import UploadPicture


def index(request):
    slide = Pictures.objects.filter(presentation ="slide")
    picture = Pictures.objects.filter(presentation ="picture").order_by('-pub_date')
    project = Pictures.objects.filter(presentation ="project").order_by('-pub_date')
    context = {'slide': slide, 'picture': picture, 'project': project}
    return render(request, 'polls/index.html', context)

def photo_landscape(request):
    picture = Pictures.objects.filter(category = 1).order_by('-pub_date')
    context = {'picture': picture}
    return render(request, 'polls/photo_landscape.html', context)

def album_uganda(request):
    picture = Pictures.objects.filter(category = 5, project ="Uganda")
    thumbnails = Pictures.objects.filter(project ="Uganda").order_by('pub_date').exclude(category = 5,)
    context = {'picture': picture, 'thumbnails': thumbnails}
    return render(request, 'polls/album_uganda.html', context)

def photo_people(request):
    picture = Pictures.objects.filter(category = 2).order_by('-pub_date')
    context = {'picture': picture}
    return render(request, 'polls/photo_people.html', context)

def wall(request):
    picture = Pictures.objects.order_by('-pub_date')
    context = {'picture': picture}
    return render(request, 'polls/wall.html', context)

def contact(request):
    return render(request, 'polls/contact.html')

def impressum(request):
    return render(request, 'polls/impressum.html')

class upload(FormView):
    template_name = 'polls/upload.html'
    form_class = UploadPicture

    def form_valid(self, form):
        profile_image = Pictures(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        return redirect('/pictures')
