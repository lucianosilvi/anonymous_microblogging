from django.db import models

class Tweet(models.Model):
    """
        Tweet data, including author's name, datetime and message.
    """
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    # Char limit higher than allowed (50) to contemplate future expansion
    message = models.CharField(max_length=100)

    def __str__(self):
        return "%s: %s " % (self.name, self.message)
