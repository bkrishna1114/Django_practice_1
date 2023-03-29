from django.urls import path
from . import views


#create url patterns here...

urlpatterns =[
    path('now/', views.now),
    path('hello/', views.hello),
    path('connection/', views.connection.as_view()),
    path('connection/<int:pk>', views.connection.as_view())
]