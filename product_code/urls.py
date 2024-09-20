from django.urls import path
from .views import HomePage, SendProductName

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('get-package-code/', SendProductName.as_view(), name='get_package_code'),
]
