from django.conf.urls import url
from . import views

urlpatterns = [
    # (...) your other url's
    url(r'^gourl_callback.html/$', views.callback, name='callback')
]
