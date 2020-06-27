from django.urls import include, path
from rest_framework import routers
from . import views
from .views import UserViewSet
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_create = UserViewSet.as_view({
    'post': 'create'
})
user_destroy = UserViewSet.as_view({
    'get': 'destroy'
})
user_update = UserViewSet.as_view({
    'post': 'partial_update'
})
user_details = UserViewSet.as_view({
    'get': 'retrieve',
})
user_login = UserViewSet.as_view({
    'post': 'login',
})
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('userslist/', user_list, name='user-list'),
    path('userpush/', user_create, name='user-create'),
    path('userpop/<int:pk>', user_destroy, name='user-destroy'),
    path('userupdate/<int:pk>', user_update, name='user-update'),
    path('userdetails/<int:pk>', user_details, name='user-details'),
    path('userlogin/', user_login, name='user-login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]