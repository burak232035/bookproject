



from django.urls import path
from bookapp.views import ApiTestView

urlpatterns = [
    path('api/test/', ApiTestView.as_view(), name='api_test_no_id'),  # ID olmadan
    path('api/test/<int:mtyp_id>/', ApiTestView.as_view(), name='api_test'),  # ID ile
]
