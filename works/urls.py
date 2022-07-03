from django.urls import path
from .views import *

urlpatterns = [
    path('', WorksView.as_view(), name='works'),
    path('work/<int:pk>/', WorksDetailView.as_view(), name='detail')
]
