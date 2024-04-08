from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=True)
    last_name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=300, blank=False, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField()

    def __str__(self):
        return self.subject
