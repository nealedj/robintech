# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
import urlparse
from core.forms import ContactForm
from google.appengine.api import mail

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('core-contact')

    def form_valid(self, form):
        mail.send_mail('david@robin-tech.co.uk', 'david@robin-tech.co.uk',
            'Contact request from %s' % form.cleaned_data['name'],
            "Email: %s. Body: %s" % (form.cleaned_data['email'],form.cleaned_data['message']))
        self.request.flash.add('info', 'Contact request sent')
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        self.request.flash.add('error', form.errors.as_ul())
        return super(ContactView, self).form_valid(form)


class ExperienceView(TemplateView):
    template_name = 'experience.html'