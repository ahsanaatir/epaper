from django.contrib import admin
from .models import CourseLevel,Subject, Unit, question_detail

# Register your models here.

admin.site.register(CourseLevel)
admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(question_detail)