from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from article.apps import ArticleConfig
from article.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = ArticleConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('articles/<int:pk>/',ArticleDetailView.as_view(), name='articles_detail'),
    path('articles/create',ArticleCreateView.as_view(), name='articles_create'),
    path('articles/<int:pk>/update',ArticleUpdateView.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='articles_delete')



# urlpatterns = [
    # path('',ProductListView.as_view(), name='home'),
    # path('products/<int:pk>/',ProductDetailView.as_view(), name='products_detail'),
    # path('products/create',ProductCreateView.as_view(), name='products_create'),
    # path('products/<int:pk>/update',ProductUpdateView.as_view(), name='products_update'),
    # path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),
    # path('contacts/',contacts,name='contacts')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)