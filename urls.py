from django.urls import path
from . import views as view

urlpatterns = [
    # (...) your other url's
    path('gourl_callback.html/', view.callback, name='callback')
]
