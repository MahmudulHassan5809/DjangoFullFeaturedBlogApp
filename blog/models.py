from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100] + '.....'

    def pub_date_pretty(self):
        return self.date_posted.strftime('%b %e %Y')

  #   def get_absolute_url(self):
		# return reverse('post-detail', kwargs={'pk': self.pk})
