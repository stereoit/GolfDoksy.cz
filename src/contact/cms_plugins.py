# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
from django.template import loader
import forms
import models
import settings

class ContactFormPlugin(CMSPluginBase):
    name = _('Contact Form Plugin') # Name of the plugin
    render_template = 'contact_form.html' # template to render the plugin with
    text_enabled = True

    def render(self, context, instance, placeholder):
        request = context['request']

        request.LANGUAGE_CODE = 'cs'

        if request.method == 'GET':
            form = forms.ContactForm()
            self.setup(request.LANGUAGE_CODE, form)
        elif request.method == 'POST':
            form = forms.ContactForm(request.POST)
            self.setup(request.LANGUAGE_CODE, form)
            if form.is_valid():
                # save model
                c = models.Contact()
                c.email     = form.cleaned_data.get('sender')
                c.phone     = form.cleaned_data.get('phone')
                c.message   = form.cleaned_data.get('message')
                c.cc_myself = form.cleaned_data.get('cc_myself')
                c.ip        = request.META['REMOTE_ADDR']
                c.save()
                # send email to us
                sender       = form.cleaned_data.get('sender')
                message      = form.cleaned_data.get('message') + "\n\n" + sender
                phone        = form.cleaned_data.get('phone')
                cc_myself    = form.cleaned_data.get('cc_myself')
                if phone != '':
                    message += "\n" + phone
                send_mail(u'AukceJinak - kontaktní formulář', message, settings.GENERAL_SUPPORT_EMAIL, [settings.GENERAL_SUPPORT_EMAIL], fail_silently=True)
                # send copy to potential customer
                if cc_myself is True:
                    contact_meta = form.contact_meta
                    message = loader.render_to_string(
                        'email/client_email_copy.txt',
                        dictionary={
                            'message'  : message,
                            'intro'    : contact_meta.email_intro,
                            'signature': contact_meta.email_signature
                        },
                        context_instance=context
                    )
                    send_mail(contact_meta.email_subject, message, settings.GENERAL_SUPPORT_EMAIL, [sender], fail_silently=True)
        else:
            raise Exception('Not supported http method')

        context.update({
            'contact': instance,
            'form'   : form
        })
        return context

    def setup(self, language_code, form):
        contact_meta = models.ContactMeta.objects.get(language_code=language_code)

        form.fields['sender'].label = contact_meta.sender_label
        form.fields['sender'].error_messages  = {
            'required' : contact_meta.sender_error_required,
            'invalid'  : contact_meta.sender_error_invalid
        }
        form.fields['phone'].label = contact_meta.phone_label
        form.fields['message'].label = contact_meta.message_label
        form.fields['message'].error_messages = {
            'required'    : contact_meta.message_error_required,
            'min_length'  : contact_meta.message_error_invalid
        }
        form.fields['cc_myself'].label = contact_meta.cc_myself_label
        form.phone_error_invalid = contact_meta.phone_error_invalid
        form.submit_button_value = contact_meta.submit_button_label
        form.message_success_msg = contact_meta.message_success_msg
        form.contact_meta = contact_meta

plugin_pool.register_plugin(ContactFormPlugin) # register the plugin
