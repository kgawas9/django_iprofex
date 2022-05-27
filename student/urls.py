from django.urls import path
from .views import CategoryView, CourseView

urlpatterns = [
    path('course-categories/', CategoryView.as_view(), name='course-categories'),
    path('course-categories/<int:id>', CategoryView.as_view(), name='course-categories-by-id'),

    path('course-details/', CourseView.as_view(), name='course-details'),
    path('course-details/<int:id>', CourseView.as_view(), name='course-details-by-id'),
]
