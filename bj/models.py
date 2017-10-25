from django.db import models

# Create your models here.




class lessons(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    vname = models.TextField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bj_lessons_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('bj_lessons_update', args=(self.pk,))


