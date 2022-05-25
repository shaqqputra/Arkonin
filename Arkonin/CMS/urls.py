from django.urls import path
from . import views
from .views import HomeView, AddProjectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('add_project/', AddProjectView.as_view(), name="add-project"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)