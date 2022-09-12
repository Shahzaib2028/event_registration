from django.urls import path
from .views import CreateEventAPI , RetreiveEventsAPI  , UpdateDeleteAPI, AttendAPI , RetreiveEventAPI

  

app_name = "manage_event"
urlpatterns = [
    path("create/", view=CreateEventAPI.as_view(), name="create"),
    path("", view=RetreiveEventsAPI.as_view(), name="events_retreive"),
    path("retrieve/<int:pk>/", view=RetreiveEventAPI.as_view(), name="event_retreive"),
    path("<int:id>/", view=UpdateDeleteAPI.as_view(), name="manage"),
    path("attend/<int:id>/", view=AttendAPI.as_view(), name="attend"),


]