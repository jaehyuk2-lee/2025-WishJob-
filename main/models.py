from django.db import models

class test(models.Model):
    create_date = models.DateTimeField(auto_now=False, auto_now_add=False)
