from django.urls import path
from pages.views import Page_Detail

from . import views
urlpatterns = [
    path('<slug:slug>', views.Page_Detail.as_view(),name='pages'),


]
