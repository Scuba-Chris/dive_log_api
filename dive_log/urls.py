from django.urls import path
from .views import DiveLogList, DiveLogDetails

urlpatterns = [
    path('divelog/', DiveLogList.as_view(), name='dive_log'),
    path('divelog/<int:pk>', DiveLogDetails.as_view(), name='dive_log_details')
]