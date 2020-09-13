from django.db import models


class Meme(models.Model):
    TYPE_CHOICES = [
        ('PROJECT', 'project'),
        ('MAINC', 'main cluster'),
        ('LARGEC', 'large cluster'),
        ('SMALLC', 'small cluster')
    ]
    STATE_CHOICES = [
        ('ONGOING', 'on-going'),
        ('STOPPED', 'finished or paused'),
        ('PLANNED', 'planned meme')
    ]
    PHASE_CHOICES = [
        ('HUMAN', 'human civilization'),
        ('MATH', 'mathematics tools'),
        ('ROBOT', 'intelligent robot'),
        ('SPACE', 'space'),
        ('REALITY', 'structure of present')
    ]

    name = models.CharField(max_length=32)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='PROJECT')
    phase = models.CharField(max_length=7, choices=PHASE_CHOICES, default='HUMAN')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    state = models.CharField(max_length=7, choices=STATE_CHOICES, default='PLANNED')

    def __str__(self):
        return self.name


class Property(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name='properties')
    property = models.CharField(max_length=32)

    def __str__(self):
        return self.property


class Detail(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    category = models.CharField(max_length=32)
    summary = models.CharField(max_length=32)
    description = models.TextField()
    remark = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.category + ' / ' + self.summary
