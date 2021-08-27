from django.contrib import admin
from .models import School_T, Department_T, Program_T, Student_T
# Register your models here.
admin.site.register(School_T)
admin.site.register(Department_T)
admin.site.register(Program_T)
admin.site.register(Student_T)

