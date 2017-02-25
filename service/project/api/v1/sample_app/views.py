from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, permissions

from core.standard_messages import errors
from core.functions import standardResponse

from sample_app.models import Artist

from .serializers import ArtistSerializer

class ArtistList(APIView):
	"""
		**GET** - lists all available artists

		**POST** - creates a new artist
	"""
	serializer_class = ArtistSerializer
	obj = Artist

	def get(self, request, *args, **kwargs):
		_array = self.obj.objects.all()
		serializer = self.serializer_class(_array, many=True)
		data = serializer.data
		if data:
			_status = status.HTTP_200_OK
		else:
			_status = status.HTTP_204_NO_CONTENT
		return Response(standardResponse(data=data), status=_status)

	def post(self, request, *args, **kwargs):
		r_data = request.data
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			obj = serializer.save()
			response = Response(standardResponse(data=serializer.data), status=status.HTTP_201_CREATED)
			response['Location'] = obj.get_absolute_url()
			return response
		else:
			return Response(standardResponse(errors=serializer.errors), status=status.HTTP_400_BAD_REQUEST)
artists_list = ArtistList.as_view()

class ArtistsDetail(APIView):
	"""
		**GET** - gets a specific artist

		**PUT** - updates an artist

		**DELETES** - deletes an artist
	"""
	serializer_class = ArtistSerializer
	obj = Artist # This is needed as model parameters does not work smoothly on the get_obj custom method

	def get(self, request, *args, **kwargs):
		# kwargs is used to get the parameters
		_id = kwargs['artist_id']
		obj = get_object_or_404(self.obj, pk=_id)
		if obj:
			serializer = self.serializer_class(obj)
			return Response(standardResponse(data=serializer.data), status=status.HTTP_200_OK)

	def put(self, request, *args, **kwargs):
		_id = kwargs['artist_id']
		obj = get_object_or_404(self.obj, pk=_id)
		if obj:
			serializer = self.serializer_class(obj, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(standardResponse(data=serializer.data), status=status.HTTP_200_OK)

	def delete(self, request, *args, **kwargs):
		_id = kwargs['artist_id']
		obj = get_object_or_404(self.obj, pk=_id)
		if obj:
			serializer = self.serializer_class(obj)
			obj.delete()
			return Response(standardResponse(data=serializer.data), status=status.HTTP_200_OK)
artist_detail = ArtistsDetail.as_view()