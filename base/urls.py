from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home , name="home") , 
    path('login/', views.loginPage, name="login"), 
    path('logout/' , views.logoutUser , name="logout"), 
<<<<<<< HEAD
    path('register/' , views.registerUser , name="register") ,    
=======
    path('register/' , views.registerUser , name="register") , 
    path('', views.home , name="home") , 
>>>>>>> e7489daedba1f0ab65e5f6023cd28be84be5a575
    path('room/<str:pk>/' , views.room , name="room") , 
    path('create-room/' , views.createRoom , name="create-room") , 
    path('update-room/<str:pk>/' , views.updateRoom , name="update-room") , 
    path('delete-room/<str:pk>/' , views.deleteRoom , name="delete-room") , 
    path('delete-message/<str:pk>/' , views.deleteMessage , name="delete-message") , 
    path('profile/<str:pk>',views.userProfile,name="user-profile")
    # path('/<str:pk>/',views.deleteRoom , name="delete-room"),
]