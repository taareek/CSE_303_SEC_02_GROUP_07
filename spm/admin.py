from django.contrib import admin
from .models import School_T, Department_T, Program_T, Student_T, Course_T, Pre_req_course_T, PLO_T, CO_T
# Register your models here.
admin.site.register(School_T)
admin.site.register(Department_T)
admin.site.register(Program_T)
admin.site.register(Student_T)
admin.site.register(Course_T)
admin.site.register(Pre_req_course_T)
admin.site.register(PLO_T)
admin.site.register(CO_T)
