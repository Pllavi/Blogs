from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title


# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=50)
    plan_edit = models.BooleanField(default=False)
    plan_post = models.BooleanField(default=False)
    plan_delete = models.BooleanField(default=False)
    plan_desc = models.TextField()

    def __str__(self):
        return self.plan_name
    

class Subscription(models.Model):
    subscription_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plans,on_delete=models.CASCADE)





