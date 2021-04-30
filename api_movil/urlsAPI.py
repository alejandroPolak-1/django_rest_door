from django.urls import path


from api_movil.views import personal_api_view, door_api_view, door_personal_api_view, personal_detail_api_view, door_detail_api_view,door_personal_detail_api_view


urlpatterns = [
      path('personal/',               personal_api_view,                  name = 'api_personal'),
      path('personal/<int:pk>/',      personal_detail_api_view,           name = 'api_personal_detail'),
      path('door/',                   door_api_view,                      name = 'api_door'),
      path('door/<int:pk>/',          door_detail_api_view,               name = 'api_door'),
      path('doorpersonal/',           door_personal_api_view,             name = 'api_door_personal'),
      path('doorpersonal/<int:pk>/',  door_personal_detail_api_view,      name = 'api_door_personal'),
      
 
]