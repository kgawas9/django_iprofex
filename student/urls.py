from django.urls import path
from .views import CartView, CategoryView, CourseView, StudentView

urlpatterns = [
    path('course-categories/', CategoryView.as_view(), name='course-categories'),
    path('course-categories/<int:id>', CategoryView.as_view(), name='course-categories-by-id'),

    path('course-details/', CourseView.as_view(), name='course-details'),
    path('course-details/<int:id>', CourseView.as_view(), name='course-details-by-id'),

    path('student-profile/', StudentView.as_view(), name='student-profile'),

    path('cart/create/', CartView.as_view(), name='create-cart'),
    path('cart/<uuid:id>/', CartView.as_view(), name='get-cart'),
]
