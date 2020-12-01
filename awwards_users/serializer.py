from rest_framework import serializers
from .models import Profile, Projects


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user', 'url', 'description', 'career', 'country', 'twitter', 'facebook',
                  'linkedin', 'instagram']

class projectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields = ['sitename', 'siteurl', 'siteimage', 'category', 'description', 'country', 'technology', 'profile']
