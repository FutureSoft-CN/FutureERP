from django.db import models

# Create your models here.
class Users_Account(models.Model):
    user_name = models.CharField(max_length=128)
    user_password = models.CharField(max_length=16)
    user_age = models.IntegerField()
    user_email = models.EmailField(unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
    class Meta:
        ordering = ['create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'