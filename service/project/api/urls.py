from django.conf.urls import url, include

from rest_framework.schemas import get_schema_view
from rest_framework_raml.renderers import RAMLRenderer, RAMLDocsRenderer

schema_view = get_schema_view(
    title='API Documentation',
    renderer_classes=[RAMLRenderer, RAMLDocsRenderer]
)

urlpatterns = [
	url(r'^v1/', include('api.v1.urls')),
	url(r'^docs/$', schema_view),
	# url(r'^docs/', include('rest_framework_docs.urls')),
]