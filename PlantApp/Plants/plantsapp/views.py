from django.shortcuts import render, redirect

from Plants.plantsapp.forms import CreateProfileForm, CreatePlantForm, DeletePlantForm, EditProfileForm
from Plants.plantsapp.models import Profile, Plant


# Create your views here.

def index(request):
    user = Profile.objects.first()
    context = {
        "user": user,
    }
    return render(request, "home-page.html", context=context)

def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            plants = Plant.objects.all()
            context = {'user': user, 'plants': plants,}
            return render(request, 'catalogue.html', context=context)
    context = {'form': form,}
    return render(request, 'create-profile.html', context=context)

def catalogue_view(request):
    plants = Plant.objects.all()
    context = {'plants': plants,}
    return render(request, 'catalogue.html', context=context)

def create_plant_view(request):
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form,}
    return render(request, 'create-plant.html', context=context)

def plant_details(request, pk):
    plant = Plant.objects.get(pk=pk)
    context = {'plant': plant,}
    return render(request, 'plant-details.html', context=context)

def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreatePlantForm(instance=plant)
    else:
        form = CreatePlantForm(request.POST, instance=Plant.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form, 'plant': plant,}
    return render(request, 'edit-plant.html', context=context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == "GET":
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        plant.delete()
        return redirect('catalogue')
    context = {'form': form, 'plant': plant, }
    return render(request, 'delete-plant.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()
    len_plants = len(plants)
    context = {'profile': profile, 'plants': plants, 'len_plants': len_plants}
    return render(request, 'profile-details.html', context=context)

def profile_edit(request):
    user = Profile.objects.first()
    if request.method == "GET":
        form = EditProfileForm(instance=user)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    context = {'form': form, 'profile': user}
    return render(request, 'edit-profile.html', context=context)

def profile_delete(request):
    user = Profile.objects.first()
    plants = Plant.objects.all()
    if request.method == "POST":
        user.delete()
        plants.delete()
        return redirect('index')
    return render(request, 'delete-profile.html')
