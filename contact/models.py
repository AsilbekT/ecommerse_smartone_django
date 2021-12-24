from django.db import models

# Create your models here.


class FeedBack(models.Model):
    title = models.CharField(max_length=25, null=True)
    user_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=40, null=True)
    text = models.TextField()

    def url_dispatcher(self):
        return f"{self.id}"

    def __str__(self):
        return self.user_name