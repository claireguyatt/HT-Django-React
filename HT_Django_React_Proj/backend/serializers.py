# django imports
from rest_framework import serializers
from django.contrib.auth.models import User

# project imports
from .models.user_models import Profile
from .models.variable_models import Variable, CategoricalVariable

# use print(repr(serializer)) in shell to see how objects are serialized

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['user', 'username', 'email', 'number', 'gender', 'dob', 'variables', 'data']

class VariablelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variable
        fields = ['name', 'prompt', 'is_continuous']
    
class CategoricalVariableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoricalVariable
        fields = ['is_binary', 'choices']

