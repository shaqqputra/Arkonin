from django.urls import path
from . import views
from .views import homeView, addProjectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('add_project/', addProjectView.as_view(), name="add-project"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)