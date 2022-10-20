from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', views.CourserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subjects/', views.SubjectListApiView.as_view(), name="subject_list"),
    path('subjects/<pk>/', views.SubjectDetailApiView.as_view(), name="subject_detail"),
    # path('courses/<pk>/enroll/', views.CourseEnrollApiView.as_view(), name='course_enroll'),

]
