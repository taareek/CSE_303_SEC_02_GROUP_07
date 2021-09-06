from django.db import models

class School_T(models.Model):
    school_id = models.CharField(max_length= 10, primary_key=True)
    school_name = models.CharField(max_length= 60)

    class Meta:
        managed = False
        db_table = 'spm_school_t'

    def __str__(self):
        return self.school_id

class Department_T(models.Model):
    department_id = models.CharField(max_length= 10, primary_key=True)
    department_name = models.CharField(max_length= 50)
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)

class Program_T(models.Model):
    program_id = models.CharField(max_length= 15, primary_key=True)
    program_name = models.CharField(max_length= 50)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE, default=None)

class Student_T(models.Model):
    student_id = models.CharField(max_length= 8, primary_key=True)
    f_name = models.CharField(max_length= 30, null=True)
    l_name = models.CharField(max_length= 30, null=True)
    email = models.EmailField(max_length = 30, null=True)
    contact_no = models.CharField(max_length= 15, null=True)
    gender = models.CharField(max_length= 6, null=True)
    date_of_birth = models.DateTimeField(null=True)
    street = models.CharField(max_length= 60, null=True)
    city = models.CharField(max_length= 30, null=True)
    state = models.CharField(max_length= 30, null=True)
    year = models.IntegerField(name='Year of admission', null=True)
    semseter = models.CharField(max_length= 10, null=True)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE, default=None)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE, default=None)

class Course_T(models.Model):
    course_id = models.CharField(max_length= 15, primary_key=True)
    course_name = models.CharField(max_length= 50)
    course_type = models.CharField(max_length= 10)
    no_of_credit = models.IntegerField(name='No of credits')
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)

class Pre_req_course_T(models.Model):
    course_id = models.CharField(max_length= 15, primary_key=True)
    Pre_req_course_id = models.ForeignKey(Course_T, on_delete=models.CASCADE)

class PLO_T(models.Model):
    plo_id = models.CharField(max_length= 10, primary_key=True)
    plo_name = models.CharField(max_length= 50)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)

class CO_T(models.Model):
    co_id = models.CharField(max_length= 10, primary_key=True)
    details = models.TextField()
    course = models.ForeignKey(Course_T, on_delete=models.CASCADE)
    plo = models.ForeignKey(PLO_T, on_delete=models.CASCADE)

class Faculty_T(models.Model):
    faculty_id = models.CharField(max_length= 10, primary_key=True)
    f_name = models.CharField(max_length= 30, null=True)
    l_name = models.CharField(max_length= 30, null=True)
    email = models.EmailField(max_length= 30, null=True)
    contact_no = models.CharField(max_length= 15, null=True)
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length= 6, null=True)
    street = models.CharField(max_length= 40, null=True)
    city = models.CharField(max_length= 20, null=True)
    state = models.CharField(max_length= 20, null=True)
    faculty_type = models.CharField(max_length= 10, null=True)


class VC_T(models.Model):
    VFaculty_id = models.ForeignKey(Faculty_T, on_delete=models.CASCADE)
    joining_date = models.DateTimeField()
    end_date = models.DateTimeField(null = True)

class GFaculty_T(models.Model):
    Gfaculty_id = models.ForeignKey(Faculty_T, on_delete=models.CASCADE)
    designation = models.CharField(max_length= 25)
    join_date = models.DateTimeField()
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE)

class Dean_T(models.Model):
    DFaculty_id = models.ForeignKey(Faculty_T, on_delete=models.CASCADE)
    joining_date = models.DateTimeField()
    end_date = models.DateTimeField()
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)

class Department_Head_T(models.Model):
    HODFaculty_id = models.ForeignKey(Faculty_T, on_delete=models.CASCADE)
    joining_date = models.DateTimeField()
    end_date = models.DateTimeField()
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE)

class Section_T(models.Model):
    section_id = models.CharField(max_length= 20, primary_key=True, default= None)
    section_no = models.IntegerField(name= 'Section No')
    semester_name = models.CharField(max_length= 10)
    year = models.IntegerField(name= 'Year')
    student_capacity = models.IntegerField(name='No of student')
    course = models.ForeignKey(Course_T, on_delete=models.CASCADE)
    faculty = models.ForeignKey(GFaculty_T, on_delete=models.CASCADE)

class Assessments_T(models.Model):
    assessments_id = models.IntegerField(name=  'Assessment ID', primary_key=True)
    assessments_name = models.CharField(max_length= 20)
    total_marks = models.FloatField(name= 'Total Marks')
    obtain_marks = models.FloatField(name= 'Obtain Marks')
    co = models.ForeignKey(CO_T, on_delete=models.CASCADE)
    section = models.ForeignKey(School_T, on_delete=models.CASCADE)

class Student_Enrollment_T(models.Model):
    student_enrollment_id = models.IntegerField(name='Enrollment ID', primary_key= True)
    section = models.ForeignKey(Section_T, on_delete=models.CASCADE)
    student = models.ForeignKey(Student_T, on_delete=models.CASCADE)
    semester = models.CharField(max_length= 10)
    year = models.IntegerField(name= 'Year')

class Evaluation_T(models.Model):
    evaluation_id = models.IntegerField(name= 'Evaluation ID', primary_key=True)
    obtain_marks = models.FloatField(name= 'Obtain Marks')
    total_marks = models.FloatField(name= 'Total Marks')
    assessments = models.ForeignKey(Assessments_T, on_delete=models.CASCADE)
    student_enrollment = models.ForeignKey(Student_Enrollment_T, on_delete=models.CASCADE)

