from django.urls import path
from .views import CreateEventAPI , RetreiveEventsAPI  , UpdateDeleteAPI

  

app_name = "manage_event"
urlpatterns = [
    path("create/", view=CreateEventAPI.as_view(), name="create"),
    path("", view=RetreiveEventsAPI.as_view(), name="events_retreive"),
    path("<int:id>/", view=UpdateDeleteAPI.as_view(), name="manage"),

]