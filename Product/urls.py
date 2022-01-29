from django.urls import path
from Product.schema import schema
from graphene_file_upload.django import FileUploadGraphQLView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    # Only a single URL to access GraphQL
    path("graphql", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
]