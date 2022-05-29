from django.contrib import admin
from django.urls import path
from . import views

app_name =  "article"


urlpatterns = [
    path('create/',views.create, name="create"),
    path('',views.articles,name = "articles"),
    path('about/',views.about,name ="about"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('comment/<int:id>',views.addComment,name = "comment"),



    ]
