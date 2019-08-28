from django.db import models

NOTE_TYPE = (
    ('t1', 'type 1'),
    ('t2', 'type 2'),
    ('t3', 'type 3')
)


class Note(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    note = models.CharField(max_length=500)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    task = models.BooleanField()
    tag = models.CharField(max_length=100)
    note_type = models.CharField(max_length=2, choices=NOTE_TYPE)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
