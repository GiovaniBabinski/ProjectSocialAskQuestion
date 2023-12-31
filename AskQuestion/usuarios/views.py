from django.shortcuts import render,get_object_or_404
from .forms import UserRegistrationForm,User

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request,'register_done.html', {'user_form':user_form})

    else:
        user_form = UserRegistrationForm()

    return render(request,'register.html',{'user_form':user_form})


