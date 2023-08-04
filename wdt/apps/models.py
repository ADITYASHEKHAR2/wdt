from django.contrib.auth.models import User


class user_model(User):
    
    def __str__(self):
        return self.username
    

