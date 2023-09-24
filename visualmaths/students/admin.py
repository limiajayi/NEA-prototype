from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.StudentUser)
admin.site.register(models.Question)
admin.site.register(models.MathsPoints)
admin.site.register(models.FurtherMathsPoints)