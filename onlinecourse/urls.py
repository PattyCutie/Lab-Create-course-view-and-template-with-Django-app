from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Add path here
    # add a route path for the popular_course_list view.
    path(route='', view=views.popular_course_list, name='popular_course_list'),
    # create a route to enroll view
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    # create a route to course_detail
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

