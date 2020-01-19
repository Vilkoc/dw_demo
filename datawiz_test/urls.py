from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from airtransport import views
from rest_framework_simplejwt import views as jwt

router = routers.DefaultRouter()
router.register(r'flights', views.FlightsViewSet)
router.register(r'bookings', views.BookingsViewSet)
router.register(r'ticket_flights', views.TicketFlightsViewSet)
router.register(r'tickets', views.BookingsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('boarding_passes/<str:ticket_no>/<int:flight_id>/', views.BoardingPassesViews.as_view()),
    path('seats/<int:aircraft_code>/<str:seat_no>/', views.SeatsDetail.as_view()),
    # path('flights/<int:pk>/', views.FlightsView.as_view())
    path('api/token/', jwt.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt.TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
