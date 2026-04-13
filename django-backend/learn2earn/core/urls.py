from django.contrib import admin
from django.urls import include, path
from strawberry.django.views import GraphQLView
from ingest.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("ingest.urls")),
    path("graphql/", GraphQLView.as_view(schema=schema, graphiql=True)),
]
