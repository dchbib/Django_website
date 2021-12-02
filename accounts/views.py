from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView


#from datetime import datetime
from .forms import SignUpForm, UserInformationUpdateForm, ContactForm


class Welcome(ListView):
    model = User
    context_object_name = 'accounts'
    template_name = 'home.html'



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user



def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid(): 

        Subject = form.cleaned_data['Subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        receive_copy = form.cleaned_data['receive_copy']
        envoi = True

    return render(request, 'contact.html', locals())



def cv(request):

    return render(request, 'cv.html', locals())
