from django.urls import include, path
from rest_framework_nested import routers

from ads.views import AdViewSet, AdDetailViewSet, CommentViewSet
# TODO настройка роутов для модели

ads_router = routers.DefaultRouter()
ads_router.register('ads', AdViewSet)
ads_router.register('ads/<int:pk>', AdDetailViewSet)
comments_router = routers.NestedDefaultRouter(ads_router, r'ads', lookup='ad')
comments_router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(ads_router.urls)),
    path('ads/<int:pk>', AdDetailViewSet.as_view({'get': 'retrieve'})),
    path('', include(comments_router.urls)),

]
