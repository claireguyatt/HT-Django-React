# django imports
from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=30)
    prompt = models.CharField(max_length=250)
    is_continuous = models.BooleanField(default=False)

    # return human-readable string for each object
    def __str__(self):
        return self.name

    # return URL for inidvidual model records
    # django automatically gives each object an id (primary key)
    def get_absolute_url(self):
        return 'model-detail-view', [str(self.id)]
    
    def check_delete(self):

        # delete from db if no longer attached to a user profile
        var = Variable.objects.get(id=self.id)
        safe_vars = ["Weather", "Happiness", "Temp", "Sleep"]
        is_safe = False
        for safe_var in safe_vars:
            if var.name == safe_var:
                is_safe = True
                break
        if is_safe == False:
            if not var.users.all():
                Variable.objects.get(id=self.id).delete()

# Variable model subclass

class CategoricalVariable(Variable):
    
    # if binary, choices are automatically Y/N
    is_binary = models.BooleanField(default=True)
    choices = models.CharField(max_length=500)
