
from django.urls import path
from .views import *
from .views import (
    Login,
    SnippetDetail,
    SnippetList,
    TodoDetailApiView,
    TodoListApiView,
    UserDetail,
    Register
)
from rest_framework.routers import SimpleRouter,DefaultRouter
from django.urls import path
router = DefaultRouter()
router.register('grouplist', Grouplist)
router.register('userlist', Userlist)
router.register('Doclist', Doclist)
router.register('Patientlist', Patientlist)
urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('product', ProductListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    path('list/<pk>/', SnippetDetail.as_view()),
    path('list', SnippetList.as_view()),
     path('lst', TodosDetail.as_view()),
    path('register/', Register.as_view(), name='auth_register'),
     path('login/', Login.as_view(), name="login"),
    path('snippets/', SnippetsList.as_view()),
    path('snippets/<int:pk>/', SnippetsDetail.as_view()),
    
    
]+router.urls