from django.db import models

# Create your models here.
JOB_TYPE  = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length = 15 , choices=JOB_TYPE)
    description = models.TextField(max_length = 1000)
    puvlished_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 1)


    def __str__(self):
        return self.title