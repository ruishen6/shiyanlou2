from django.db import models

# Create your models here.
from datetime import datetime

class Upload(models.Model):
    DownloadDocount = models.IntegerField(verbose_name=u"visit_times",default=0)
    code = models.CharField(max_length=8,verbose_name=u"code")
    Datetime = models.DateTimeField(default=datetime.now,verbose_name=u"add_time")
    path = models.CharField(max_length=32,verbose_name=u"download_path")
    name = models.CharField(max_length=32,verbose_name=u"file_name",default="")
    Filesize = models.CharField(max_length=10,verbose_name=u"file_size")
    PCIP = models.CharField(max_length=32,verbose_name=u"IP_address",default="")

    class Meta():
        verbose_name="download"
        db_table = "download"

    def __str__(self):
        return self.name
