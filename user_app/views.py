import time
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .models import CustomUserProfile
from .forms import UpdateProfileForm
# Create your views here.
@login_required
def profile(request):
    template_name = 'user_app/profile.html'
    profile = get_object_or_404(CustomUserProfile, id=request.user.id)

    # request
    if request.method == 'POST':
        # print(request.POST, request.FILES)
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = profile.id
            post.save()
            time.sleep(4)
            data = {
                "full_name": f"{post.first_name} {post.last_name}", "occupation": post.occupation,
                "date_of_birth": post.date_of_birth.strftime("%B %d %G"), "gender": post.gender,
                "country_flag": post.country.flag, "country_name": post.country.name,
                "phone_number": str(post.phone_number), "photo": f"/media/{post.photo}",
            }
            # print(data)
            return JsonResponse({'data':data}, status=200)
            # return redirect('user_app:profile')

    context = {
        'profile': profile,
        'profile_update_form': UpdateProfileForm(instance=profile)
    }

    return render(request, template_name, context)