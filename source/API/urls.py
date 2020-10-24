from django.urls import path, include
from .views import get_token_view, FavoriteAddView, FavoriteRemoveView


app_name = 'API'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('photo/<int:pk>/add', FavoriteAddView.as_view(), name='fav_ad'),
    path('photo/<int:pk>/remove', FavoriteRemoveView.as_view(), name='fav_re')
]
