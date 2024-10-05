from django.urls import path

from user_app.api import views

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
    ## URLS WHEN DJANGO WEB TOKENS
    
    # path('login', obtain_auth_token, name='login'),
    
    path('register', views.RegistrationAPI.as_view(), name='register'),  ## THIS URL WORKS FOR JWT REGISTER AS WELL, AS ITS PRIMARY FUNCTION IS TO REGISTER USERS,
                                                                         ## IN THE VIEW FUNCTION OF THIS, WE HAVE MADE CHANGES TO GENERATE JWT TOKENS
    
    # path('logout', views.LogoutAPI.as_view(), name='logout'),
    
    ## URLS FOR JWT 
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
