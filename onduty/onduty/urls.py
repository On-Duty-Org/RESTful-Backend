"""onduty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# We add the API endpoints here

from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from police import views as policeviews
from zones import views as zoneviews
from webapp import views as landingviews
from alerts import views as alertviews
from allocations import views as allocationviews

urlpatterns = [
    path('', landingviews.LandingPage.as_view()),
    path('admin/', admin.site.urls),
    path('police/', policeviews.police.as_view()),  # will chose the appropriate view function based on get/post request. We don't need to specify that	
    path('police/<int:id>/', policeviews.policebyid.as_view()),  # will chose the appropriate view function based on get/post request. We don't need to specify that 
    path('alert/', alertviews.alert.as_view()),
    path('zone/', zoneviews.zone.as_view()),	
    path('zone/<int:id>/', zoneviews.zonebyid.as_view()),
    path('allocation/', allocationviews.allocation.as_view()),	
    path('allocation/<int:id>/', allocationviews.allocationbyid.as_view()),
]
