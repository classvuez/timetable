from django.contrib import admin
from .models import Administrator, Class, Consultation, Course, Department, Enrollment
from .models import Faculty, Lecturer, Student, Subject, UserProfile, Venue

# Register your models here.

admin.site.register(Administrator)
admin.site.register(Class)
admin.site.register(Consultation)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Enrollment)
admin.site.register(Faculty)
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(UserProfile)
admin.site.register(Venue)
