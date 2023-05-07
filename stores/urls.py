from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from .views import store_items

urlpatterns = [
    path('stores/', views.StoreViewCreate.as_view(), name='stores'),
    # path('stores/<int:store_id>/items/', views.store_items,name='store_items'),
    path('stores/<int:store_id>/items/', views.ItemViewCreate.as_view(),name='store_items'),
    # path('items/<str:id>/', views.items, name='items'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
