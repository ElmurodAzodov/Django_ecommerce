
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from store.views import *
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path("", ProductListView.as_view(), name="products_view"),
    path("add_product", AddProductView.as_view(), name="add_product"),
    path('product/<slug:slug>/', ProductDetailsView.as_view(), name='product_detail'),
    path("update_product/<int:pk>", ProductUpdateView.as_view(), name="update_product"),
    path("delete_product/<int:product_id>", delete_product, name="delete_product"),
    
    # path("send_email/", send_email_view, name="send_email_view"),
    # path('send_email/', send_email, name='send_email'),
    
]

# To display images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

