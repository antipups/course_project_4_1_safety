from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from mail.models import Mails
from mailing_api.mailing import check_mail


class MailListView(LoginRequiredMixin, ListView):
    template_name = 'mail/list.html'
    context_object_name = 'mails'

    model = Mails

    def get_queryset(self):
        return Mails.objects.filter(user=self.request.user)


class MailCreateForm(ModelForm):
    class Meta:
        model = Mails
        fields = ('mail_title', 'login', 'password')

    def clean(self):
        login, password = self.cleaned_data['login'], self.cleaned_data['password']
        if error_text := check_mail(login=login,
                                    password=password):
            raise ValidationError(error_text.decode('utf-8'))
        return self.cleaned_data


class CreateMail(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    model = Mails
    form_class = MailCreateForm

    def get_success_url(self):
        return reverse_lazy('mail:mails_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CreateMail, self).form_valid(form)

