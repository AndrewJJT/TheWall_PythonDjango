from django.db import models
from ..user_info.models import User

# Create your models here.
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="usermessages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message,related_name="messages")
    user = models.ForeignKey(User, related_name="usercomments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
  
    
