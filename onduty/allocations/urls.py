from django.urls import path
from . import views
from .views import allocationsCreateView

urlpatterns = [
    path('', allocationsCreateView.as_view(), name='allocations-create'),
]