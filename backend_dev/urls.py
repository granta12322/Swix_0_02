from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, VenueViewSet

router = DefaultRouter()
router.register(r'events',views.EventViewSet)
router.register(r'venues',views.VenueViewSet)
router.register(r'tickets',views.TicketViewSet)



urlpatterns = router.urls