from django.contrib import admin
from django.urls import path
from api.views import SignupRydeUserView, LoginRydeUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/'. SignupRydeUserView.as_view()),
    path('login/', LoginRydeUserView.as_view()),
]
