from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from landing.forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.safestring import mark_safe

## --User Creation

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    print('gg')
    print('asasass')
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register')
    def form_valid(self, form):
        messages.success(self.request,mark_safe("회원가입이 완료되었습니다.<p>관리자 동의 후에 로그인 하실 수 있습니다.</p> 로그인 하시겠습니까?&ensp;"
                                                "<button class='IBMPlexSansKR-Text bold' onclick=location.href='/accounts/login'>로그인</button>"))
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'