
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:project_id>/', views.project, name='project'),
    path('property/<int:pk>/',PropertyDetailView.as_view(), name = 'property-detail'),
    path('property/<int:pk>/update/',PropertyUpdateView.as_view(), name = 'property-update'),
    path('property/<int:pk>/delete/',PropertyDeleteView.as_view(), name = 'property-delete'),
    path('profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),
    path('user/<str:username>/',UserPropertyListView.as_view(), name = 'user-projects'),
    path('search/',views.hup_find, name = 'search'),
    path('api/properties/', views.PropertyList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)