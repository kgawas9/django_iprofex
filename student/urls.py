from django.urls import URLPattern, path
from .views import CourseSerializerView

urlpatterns = [
    path('course-details/', CourseSerializerView.as_view(), name='course-details'),
]
