from django.urls import path
from . import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.endpoints, name='home'),
    path('advocates/', views.advocate_list, name="advocates"),
    path('advocates/<str:username>/', views.AdvocateDetail.as_view(), name='advocate_detail'),
    path('companies/', views.companies_list, name='companies'),
    
]
