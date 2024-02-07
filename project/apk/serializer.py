from rest_framework import serializers
from apk.models import WatchList,StreamPlatform




# shortcut method to create a serializers 

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model =WatchList
        fields ='__all__'



# shortcut method to create a serializers 

class StreamPlatformserializer(serializers.ModelSerializer):
    class Meta:
        model =StreamPlatform
        fields='__all__'












#### long method to create a serializer #################

# class WatchListSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField( max_length=50)
#     storyline =serializers.CharField(max_length = 150)
#     # platform=serializers.ForeignKey('StreamPlatform',on_delete=models.CASCADE)
#     active=serializers.BooleanField(default=True)
#     created=serializers.DateField()
    
    
    
# # for create a WatchListSerializer     
#     def create(self,validated_data):
#         # Create and return a new `WatchList` instance, given the validated data.
#         return WatchList.objects.create(**validated_data)



# # for update a WatchListSerializer
#     def update(self, instance, validated_data):
#         # Update and return an existing `StreamPlatform` instance, given the validated data.
#             instance.title = validated_data.get('title', instance.title)
#             instance.storyline = validated_data.get('storyline', instance.storyline)
#             instance.active = validated_data.get('active', instance.active)
#             instance.created = validated_data.get('created', instance.created)
#             instance.save()
#             return instance





#             this is long method to create a serializer    #
# class StreamPlatformserializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=50)
#     about=serializers.CharField( max_length=50)
#     website=serializers.URLField(max_length=200)


# # for create a StreamPlatformserializer     
#     def create(self, validated_data):
#             #Create and return a new `StreamPlatform` instance, given the validated data.
#         return StreamPlatform.objects.create(**validated_data)



# # for update a StreamPlatformserializer
#     def update(self, instance, validated_data):
#         # Update and return an existing `StreamPlatform` instance, given the validated data.
#             instance.name = validated_data.get('name', instance.name)
#             instance.about = validated_data.get('about', instance.about)
#             instance.website = validated_data.get('website', instance.website)
#             instance.save()
#             return instance
