from django.db import models

class Test(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test_table'

    def __str__(self):
        return f"{self.name} ({self.age})"