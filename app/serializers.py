
from rest_framework import serializers

from .models import Article, Communitie, Course, Developer, Project, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        

class CommunitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communitie
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class DevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'