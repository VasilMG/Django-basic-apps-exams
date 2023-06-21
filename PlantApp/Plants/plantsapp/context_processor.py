from Plants.plantsapp.models import Profile


def user(request):
    if Profile.objects.first():
        return Profile.objects.first().__dict__
    return {'None': 'None'}