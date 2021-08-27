from django.db import models

class School_T(models.Model):
    school_id = models.CharField(max_length= 5, primary_key=True)
    school_name = models.CharField(max_length= 30)

class Department_T(models.Model):
    department_id = models.CharField(max_length= 10, primary_key=True)
    department_name = models.CharField(max_length= 30)
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)

class Program_T(models.Model):
    program_id = models.CharField(max_length= 5, primary_key=True)
    program_name = models.CharField(max_length= 30)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE, default=None)

class Student_T(models.Model):
    student_id = models.CharField(max_length= 8, primary_key=True)
    f_name = models.CharField(max_length= 20)
    l_name = models.CharField(max_length= 20)
    email = models.EmailField(max_length = 30)
    contact_no = models.CharField(max_length= 15)
    gender = models.CharField(max_length= 6)
    date_of_birth = models.DateTimeField()
    street = models.CharField(max_length= 30)
    city = models.CharField(max_length= 20)
    state = models.CharField(max_length= 20)
    year = models.IntegerField(name='Year of admission', null=True)
    semseter = models.CharField(max_length= 10)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE, default=None)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE, default=None)

class Course_T(models.Model):
    course_id = models.CharField(max_length= 6, primary_key=True)
    course_name = models.CharField(max_length= 25)
    course_type = models.CharField(max_length= 10)
    no_of_credit = models.IntegerField(name='No of credits')
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)

class Pre_req_course_T(models.Model):
    course_id = models.CharField(max_length= 6, primary_key=True)
    Pre_req_course_id = models.ForeignKey(Course_T, on_delete=models.CASCADE)

class PLO_T(models.Model):
    plo_id = models.CharField(max_length= 5, primary_key=True)
    plo_name = models.CharField(max_length= 30)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)

class CO_T(models.Model):
    co_id = models.CharField(max_length= 5, primary_key=True)
    details = models.TextField()
    course = models.ForeignKey(Course_T, on_delete=models.CASCADE)
    plo_id = models.ForeignKey(PLO_T, on_delete=models.CASCADE)



