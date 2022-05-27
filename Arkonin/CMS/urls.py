from django.urls import path
from . import views
from .views import HomeView, AddProjectView, ProjectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # URL Project
    path('add_project/', AddProjectView.as_view(), name="add-project"),
    path('project/', ProjectView.as_view(), name="project"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)