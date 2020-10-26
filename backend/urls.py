from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

# router = routers.DefaultRouter()
# router.register(r'status_lead', views.StatusLeadViewset)
# router.register(r'lead', views.LeadViewset)
# router.register(r'customer', views.CustomerViewset)
# router.register(r'opportunity', views.OpportunityViewset)
# router.register(r'users', views.UserViewset)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    path('leads/', views.LeadsList.as_view()),
    path('leads/<int:pk>', views.LeadsDetail.as_view()),
    path('users/', views.UserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)