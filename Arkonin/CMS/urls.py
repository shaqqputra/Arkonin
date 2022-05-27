from django.urls import path
from . import views
from .views import HomeView, AddProjectView, ProjectView, UpdateProjectView, AddEmployeeView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # URL Project
    path('add_project/', AddProjectView.as_view(), name="add-project"),
    path('project/', ProjectView.as_view(), name="project"),
    path('project/edit/<int:pk>', UpdateProjectView.as_view(), name="update-project"),
    path('project/delete/<int:id>', views.delete, name='delete'),

    # URL Employee
    path('add_employee/', AddEmployeeView.as_view(), name="add-employee"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)