from django.urls import path
from . import views

urlpatterns = [
    path('category-list/',views.get_category_list),
    path('category-detail/<int:id>/',views.get_category_detail),
    path('category/<int:id>/',views.get_category_post_list),#qo`shimcha
    path('post-list/',views.get_post_list),
    path('post-detail/<int:id>/',views.get_post_detail),
    path('create-comment/<int:id>/',views.create_comment),
    path('get-post-comment/<int:id>/',views.get_post_comment),
    path('get-comment/<int:id>/',views.get_comment),
]
