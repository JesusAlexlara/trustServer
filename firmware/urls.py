from django.urls import path
from .views import ServerUpdate, EncoderUpdate, ServerCheck, EncoderCheck

urlpatterns = [

    path('update_sv/<int:buildVersion>', ServerUpdate.as_view()),
    path('update_ec/<int:buildVersion>', EncoderUpdate.as_view()),
    path('check_sv/<int:buildVersion>', ServerCheck.as_view()),
    path('check_ec/<int:buildVersion>', EncoderCheck.as_view()),

]
