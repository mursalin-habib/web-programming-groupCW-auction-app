"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic.base import TemplateView

from mysite import settings
from users.api.views import CurrentUserView, UserUpdateView
from rest_framework.routers import DefaultRouter
from auctions.api.views import ItemModelViewSet, ItemCommentModelViewSet
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from users.views import HomeView, SignUpView

router = DefaultRouter()
router.register(r'items', ItemModelViewSet, basename="item")
router.register(r'comments', ItemCommentModelViewSet, basename="comments")

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('accounts/', include("django.contrib.auth.urls")),
                  # path('', TemplateView.as_view(template_name='home.html'), name='home'),
                  # path("accounts/", include("accounts.urls")),
                  path("", HomeView.as_view(), name="dashboard"),
                  path('signup/', SignUpView.as_view(), name='signup'),

                  path("login/", LoginView.as_view(
                      template_name='registration/login.html', redirect_authenticated_user=True),
                       name='login'),
                  path("logout/", LogoutView.as_view(), name="logout"),
                  path('logged_in_user/', CurrentUserView.as_view()),
                  path('user/update/<int:pk>/', UserUpdateView.as_view()),

                  path('api/', include(router.urls)),

                  path("item-list/", HomeView.as_view()),
                  path("profile/", HomeView.as_view()),
                  path("add-item/", HomeView.as_view()),
                  path("item/", HomeView.as_view()),
                  path("item-list/detail/<int:id>", HomeView.as_view()),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
