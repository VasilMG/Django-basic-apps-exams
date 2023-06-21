from django.shortcuts import render, redirect

from CarCollection.project.forms import CreateProfileForm, CreateCarForm, DeleteCarForm, EditProfileForm
from CarCollection.project.models import Profile, Car


# Create your views here.

def  index_view(request):
    user = Profile.objects.first()
    context = {'user': user,}
    return render(request, 'index.html', context=context)

def  profile_crete_view(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form,}
    return render(request, 'profile-create.html', context=context)

def  catalogue_view(request):
    user = Profile.objects.first()
    cars = Car.objects.all()
    number = len(cars)
    context = {
        "user": user,
        'cars': cars,
        'number': number,
    }
    return render(request, 'catalogue.html', context=context)

def  car_create_view(request):
    if request.method =="GET":
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    return render(request, 'car-create.html', context={"form": form,})

def  car_details_view(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'car-details.html', context={'car': car,})

def  edit_car_view(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        form = CreateCarForm(instance=car)
    else:
        form = CreateCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    return render(request, 'car-edit.html', context={'form': form},)


def  delete_car_view(request, pk):
    car = Car.objects.get(pk=pk)
    form = DeleteCarForm(instance=Car)
    if request.method =="POST":
        car.delete()
        return redirect('catalogue')
    return render(request, 'car-delete.html', context={'form': form,})

def  profile_details_view(request):
    user = Profile.objects.first()
    cars = Car.objects.all()
    total = 0
    for car in cars:
        total+=car.price
    return render(request, 'profile-details.html', context={'user': user, 'total': total})

def  edit_profile_view(request):
    user = Profile.objects.first()
    if request.method == "GET":
        form = EditProfileForm(instance=user)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    return render(request, 'profile-edit.html', context={"form": form,})

def  delete_profile_view(request):
    user = Profile.objects.first()
    if request.method == "POST":
        user.delete()
        return redirect('index')
    return render(request, 'profile-delete.html')

