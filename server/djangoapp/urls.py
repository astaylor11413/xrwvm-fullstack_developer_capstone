from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for registration
    path(route='register', view=views.registration, name='register'),

    # path for login
    path(route='login', view=views.login_user, name='login'),

    #path for logout
    path(route='logout', view=views.logout_user, name='logout'),

    # path for dealer reviews view
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews,name='dealer_review')

    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review')

    #path for retrieving list of all cars
    path(route='get_cars', view=views.get_cars, name ='getcars'),

    #paths for get all dealers and get all dealers from a chosen state
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='dealers_by_state'),

    #path for retrieving all dealer details for a dealer based on their dealer id
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
