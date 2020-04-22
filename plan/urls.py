from django.urls import path
from plan.views import Requirements, RoughRequirements, DetailedRequirements

urlpatterns = [
    path("requirements/", Requirements.as_view()),
    path("rough_requirements/", RoughRequirements.as_view()),
    path("detailed_requirements/", DetailedRequirements.as_view()),
]