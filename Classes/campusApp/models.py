from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=False, null=False)
    location = models.CharField(max_length=60, default="", blank=False, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # Model Manager
    object = models.Manager()


    def __str__(self):
        display_campus = '{0.campus_name}'
        return display_campus.format(self)

    # Meta class to display University Campus in browser on admin page
    class Meta:
        verbose_name_plural = "University Campus"

