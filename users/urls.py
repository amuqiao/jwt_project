from django.urls import path
from .views import UserSignUpView, UserSignInView, UserMeView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('signin/', UserSignInView.as_view(), name='signin'),
    path('me/', UserMeView.as_view(), name='me'),
]
