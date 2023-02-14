# django imports
from django.db import models
from django.contrib.auth.models import User

# project imports
from .variable_models import Variable

GENDER_CHOICES = (
    ("Woman", "Woman"),
    ("Man", "Man"),
    ("Non binary", "Non binary"),
    ("Other", "Other")
)

class ProfileManager(models.Manager):
        
    # new user
    def create_profile(self, user, username, email, number, gender, dob):

        profile = self.create(user=user, username=username, email=email, number=number, gender=gender, dob=dob)
        
        # add default variables
        default_vars = [1, 2, 3, 4]
        for var_key in default_vars:
            v = Variable.objects.get(pk=var_key)
            profile.variables.add(v)
        
        return profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, help_text='Required. Enter your email.', unique=True)
    number = models.CharField(max_length=11, help_text='Enter your phone number.')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Woman')
    dob = models.DateField()
    variables = models.ManyToManyField(Variable, related_name="users")
    data = models.JSONField(default=dict)

    objects = ProfileManager()

    # return human-readable string for each object
    def __str__(self):
        return (self.username)