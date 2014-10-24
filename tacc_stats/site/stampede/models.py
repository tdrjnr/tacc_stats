"""The database models of tacc stats"""

from django.db import models
from django.forms import ModelForm

class Job(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid = models.BigIntegerField(null=True)
    project = models.CharField(max_length=128)
    start_time =  models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    start_epoch =  models.PositiveIntegerField(null=True)
    end_epoch = models.PositiveIntegerField(null=True)
    run_time = models.PositiveIntegerField(null=True)
    queue_time = models.PositiveIntegerField(null=True)
    queue = models.CharField(max_length=16, null=True)
    name =  models.CharField(max_length=128, null=True)
    status = models.CharField(max_length=16, null=True)
    nodes = models.PositiveIntegerField(null=True)
    cores = models.PositiveIntegerField(null=True)
    wayness = models.PositiveIntegerField(null=True)
    path =  models.FilePathField(max_length=128, null=True)
    date = models.DateField(db_index=True,null=True)
    user = models.CharField(max_length=128, null=True)
    exe = models.CharField(max_length=128, null=True)
    cwd = models.CharField(max_length=128, null=True)
    threads = models.BigIntegerField(null=True)

    cpi = models.FloatField(null=True)
    mbw = models.FloatField(null=True)
    idle = models.FloatField(null=True)
    cat = models.FloatField(null=True)
    mem = models.FloatField(null=True)
    packetrate = models.FloatField(null=True)
    packetsize = models.FloatField(null=True)
    GigEBW = models.FloatField(null=True)
    flops = models.FloatField(null=True)
    VecPercent = models.FloatField(null=True)

    def __unicode__(self):
        return str(self.id)

    def color(self):

        if self.status == 'COMPLETED':
            ret_val = "lightblue"
        elif self.status == 'FAILED':
            ret_val = "red"
        else:
            ret_val = "silver"

        return ret_val

class Host(models.Model):
    name = models.CharField(max_length=128)
    jobs = models.ManyToManyField(Job)
    class Meta: ordering = ('name',)

    def __unicode__(self):
        return str(self.name)

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['id']
