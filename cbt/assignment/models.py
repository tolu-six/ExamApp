from django.db import models
from django.urls import reverse


NO = 0
YES = 1

CHOICE = (
    ('', 'Choose...'),
    (YES, 'Yes'),
    (NO, 'No'),
)

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name   

class Assignment(models.Model):
    name = models.CharField(max_length=200)
    instruction = models.TextField(max_length=500)
    #duration = models.DurationField()
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    show_result = models.IntegerField(choices=CHOICE)
    show_instruction = models.IntegerField(choices=CHOICE)
    is_active = models.IntegerField(choices=CHOICE)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    #created_by = models.IntegerField()
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
