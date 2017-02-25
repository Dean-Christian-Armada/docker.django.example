from rest_framework import serializers

from sample_app.models import Artist

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = '__all__'