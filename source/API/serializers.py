# from rest_framework.serializers import ModelSerializer
# from webapp.models import Photo
#
#
# class PhotoSerializer(ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = ['id', 'sign', 'img', 'author', 'date', 'favorites']
#         read_only_fields = ('author', 'img')
#
#     def create(self, validated_data):
#         return Photo.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance


