from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title='Tasks API',
    description='API for managing tasks',
)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/tasks/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('schema/', schema_view, name='openapi-schema'),
]