"""
URLs for django_app.
"""
from django.urls import path, re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from django_app.views import CourseListAPIView
urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="django_app/base.html")),
    path('list/', CourseListAPIView.as_view(), name='course_list')
]
