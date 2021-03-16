from django.db import models

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    work_type = models.CharField(max_length=200)
    completion_status = models.CharField(max_length=10)
    project_banner = models.FilePathField(path='/images')
    project_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.project_name