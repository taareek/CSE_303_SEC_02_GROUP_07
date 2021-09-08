from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import School_T, Department_T, Program_T, Student_T, Course_T, Pre_req_course_T, PLO_T, CO_T, Faculty_T, VC_T, GFaculty_T, Department_Head_T, Dean_T, Section_T, Student_Enrollment_T, Assessments_T, Evaluation_T
# Register your models here.
#admin.site.register(School_T)
#admin.site.register(Department_T)
#admin.site.register(Program_T)
#admin.site.register(Student_T)
#admin.site.register(Course_T)
#admin.site.register(Pre_req_course_T)
#admin.site.register(PLO_T)
#admin.site.register(CO_T)
#admin.site.register(Faculty_T)
#admin.site.register(VC_T)
#admin.site.register(Dean_T)
#admin.site.register(Department_Head_T)
#admin.site.register(GFaculty_T)
#admin.site.register(Section_T)
#admin.site.register(Assessments_T)
#admin.site.register(Student_Enrollment_T)
#admin.site.register(Evaluation_T)

# To upload data using excel sheet 

@admin.register(School_T)
class SchoolData(ImportExportModelAdmin):
    list_display = ("school_id", "school_name")
    pass
admin.register(School_T)

@admin.register(Department_T)
class DepartmentData(ImportExportModelAdmin):
    list_display = ("department_id", "department_name", "school_id")
    pass
admin.register(Department_T)

@admin.register(Program_T)
class ProgramData(ImportExportModelAdmin):
    list_display= ("program_id", "program_name", "department_id")
    pass
admin.register(Program_T)

@admin.register(Student_T)
class StudentData(ImportExportModelAdmin):
    #list_display = ("student_id", "f_name", "l_name", "email", "contact_no", "gender", "date_of_birth", "street", "city", "state", "year", "semester", "program_id", "department_id")
    pass
admin.register(Student_T)

@admin.register(Course_T)
class CourseData(ImportExportModelAdmin):
    #list_display = ("course_id", "course_name" , "course_type", "No Of Credits", "program_id" )
    pass
admin.register(Course_T)

@admin.register(Pre_req_course_T)
class PreReqCrsData(ImportExportModelAdmin):
    pass
admin.register(Pre_req_course_T)

@admin.register(PLO_T)
class PLOData(ImportExportModelAdmin):
    pass
admin.register(PLO_T)

@admin.register(CO_T)
class COData(ImportExportModelAdmin):
    pass
admin.register(CO_T)

@admin.register(Faculty_T)
class FacultyData(ImportExportModelAdmin):
    pass
admin.register(Faculty_T)

@admin.register(VC_T)
class VcData(ImportExportModelAdmin):
    pass
admin.register(VC_T)

@admin.register(Dean_T)
class DeanData(ImportExportModelAdmin):
    pass
admin.register(Dean_T)

@admin.register(Department_Head_T)
class DepartmentHeadData(ImportExportModelAdmin):
    pass
admin.register(Department_Head_T)

@admin.register(GFaculty_T)
class GFacultyData(ImportExportModelAdmin):
    pass
admin.register(GFaculty_T)


@admin.register(Section_T)
class SectionData(ImportExportModelAdmin):
    pass
admin.register(Section_T)
@admin.register(Assessments_T)
class AssessmentData(ImportExportModelAdmin):
   pass
admin.register(Assessments_T)

@admin.register(Student_Enrollment_T)
class StdEnronmentData(ImportExportModelAdmin):
    pass
admin.register(Student_Enrollment_T)

@admin.register(Evaluation_T)
class EvaluationData(ImportExportModelAdmin):
    pass
admin.register(Evaluation_T)
