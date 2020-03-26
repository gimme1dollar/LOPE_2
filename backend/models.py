from django.db import models


class Meme(models.Model):
    TYPE_CHOICES = [
        ('PROJECT', 'project'),
        ('CLUSTER', 'cluster')
    ]
    STATE_CHOICES = [
        ('ONGOING', 'on-going'),
        ('STOPPED', 'finished or paused'),
        ('PLANNED', 'planned meme')
    ]

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='PROJECT')
    level = models.IntegerField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    state = models.CharField(max_length=7, choices=STATE_CHOICES, default='PLANNED')

    def __str__(self):
        return self.name
