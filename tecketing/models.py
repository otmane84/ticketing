from django.db import models


class Ticket(models.Model):
    submitter = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return u'%s %s %s' % (self.submitter, self.created_at, self.body)
       

