from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


def validae_authorMail(value):
    if value.endswith('@gmail.com'):
        return value
    else:
        raise ValidationError("This is not a COrrect format for mail")
    
def validate_mobile_number(value):
    if not value.startswith('+'):
        raise ValidationError(_('Phone number must start with +'))
    if not value[1:].isdigit():
        raise ValidationError(_('Invalid characters in the phone number. Only digits are allowed after the + sign.')) 
    
class Author(models.Model):
    name = models.CharField(max_length = 120)
    display_pic = models.ImageField(upload_to="images")
    email = models.CharField(max_length=200,null=True,blank=True,validators=[validae_authorMail])
    contact_no = models.CharField(max_length=200,null=True,blank=True,validators=[validate_mobile_number])
    def __str__(self):
        return self.name
    



class Blog(models.Model):
    title = models.CharField(max_length = 120)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    desc = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.title    
    

