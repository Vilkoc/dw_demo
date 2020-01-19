from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from airtransport import views
from rest_framework_simplejwt import views as jwt

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'flights', views.FlightsView)
# router.register(r'flight_views', views.FlightsViewView)
# router.register(r'boarding_passes', views.BoardingPasses)
router.register(r'bookings', views.Bookings)
# router.register(r'seats', views.Seats)
router.register(r'ticket_flights', views.TicketFlights)
router.register(r'tickets', views.Bookings)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('boarding_passes/', views.BoardingPassesList.as_view()),
    path('boarding_passes/<str:ticket_no>/<int:flight_id>/', views.BoardingPassesViews.as_view()),
    path('seats/<int:aircraft_code>/<str:seat_no>/', views.SeatsDetail.as_view()),
    # path('flights/<int:pk>/', views.FlightsDetail.as_view())
    path('api/token/', jwt.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/get_token/', views.get_token, name='get_new_token'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
