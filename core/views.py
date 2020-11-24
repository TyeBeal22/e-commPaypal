from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.views import generic
from cart.models import Order, Product
from .forms import ContactForm
from cart.models import Product
from django_anysign import api as django_anysign
from django_docusign import api as django_docusign

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse




class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context

class HomeView(generic.TemplateView):
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        messages.info(self.request, "Thanks for getting in touch")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
            Received message below from {name}, {email}
            _______________________

            {message}

            """
        send_mail(
            subject="Received contact form submission",
            message = full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)


