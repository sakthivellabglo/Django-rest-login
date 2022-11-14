
from django.urls import path, include
from .views import ProductListApiView, login,logout
from knox import views as knox_views
from .views import (
    Login,
    Logout,
    SnippetDetail,
    SnippetList,
    TodoDetailApiView,
    TodoListApiView,
    UserDetail,
   
    Register

)
from django.urls import path

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('product', ProductListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    path('list/<pk>/', SnippetDetail.as_view()),
    path('list', SnippetList.as_view()),
     path('lst/<pk>/', UserDetail.as_view()),
    path('register/', Register.as_view(), name='auth_register'),
     path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('api/login', login,),
    path('api/logout', logout,),
   
]