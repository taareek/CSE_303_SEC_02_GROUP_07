from django.db import models

class school_T(models.Model):
    school_id = models.CharField(max_length= 5, primary_key=True)
    school_name = models.CharField(max_length= 30)
    
