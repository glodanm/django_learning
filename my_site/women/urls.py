from django.urls import path

from .views import * 

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),

    # path('cats/<int:cat_id>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})', archive)
]