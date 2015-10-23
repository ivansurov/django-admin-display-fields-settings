from django.contrib.auth.models import User
from django.db import models


class DisplaySettings(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, verbose_name=u"User", null=False, blank=False)
    app_label = models.CharField(max_length=100, verbose_name=u"Application label", null=False, blank=False)
    model = models.CharField(max_length=100, verbose_name=u"Model name", null=False, blank=False)
    view = models.CharField(max_length=100, verbose_name=u"View name", null=False, blank=False)
    settings = models.TextField(default=None, verbose_name=u"Settings", null=True, blank=True)

    class Meta:
        unique_together = (("user_id", "app_label", "model", "view"),)
        verbose_name = u"Settings Display Model"
        verbose_name_plural = u"Settings Display Model"


    def __unicode__(self):
        return "%s|%s|%s" % (self.user_id, self.app_label, self.model)