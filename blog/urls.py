from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('<int:id>/', views.post_detail, name='post_detail'),

    path('<int:post_id>/comment/',
         views.post_comment, name='post_comment'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),

]