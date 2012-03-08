from django.db import models

class Contact(models.Model):
    email     = models.CharField(max_length=255)
    phone     = models.CharField(max_length=40, blank=True)
    message   = models.TextField()
    cc_myself = models.BooleanField(default=True)
    ip        = models.CharField(max_length=15)
    inserted  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s  (%s)' % (self.email, self.ip)

class ContactMeta(models.Model):

    language_code       = models.CharField(max_length=255, unique=True)

    sender_label        = models.CharField(max_length=255)
    phone_label         = models.CharField(max_length=40)
    message_label       = models.CharField(max_length=255)
    cc_myself_label     = models.CharField(max_length=255)
    submit_button_label = models.CharField(max_length=255)

    sender_error_required  = models.TextField()
    sender_error_invalid   = models.TextField()
    phone_error_invalid    = models.TextField()
    message_error_required = models.TextField()
    message_error_invalid  = models.TextField()

    message_success_msg    = models.TextField()

    email_subject   = models.TextField()
    email_intro     = models.TextField()
    email_signature = models.TextField()

    def __unicode__(self):
        return self.language_code