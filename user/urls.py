from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

# DefaultRouter的url在末尾会自动加/
router = DefaultRouter()
router.register("api/user", views.UserViewSet, basename="user")

urlpatterns = [
    path('api/login/account', obtain_jwt_token),
    path('api/currentUser', views.CurrentUser.as_view()),

    re_path("", include(router.urls)),
]
