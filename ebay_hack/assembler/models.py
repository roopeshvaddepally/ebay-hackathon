from django.db import models

class Users(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    def __unicode__(self):
        return "%s: %s" % (user_id, product_id)

