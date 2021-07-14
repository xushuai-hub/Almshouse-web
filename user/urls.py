from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from user import user_views

router = DefaultRouter()
router.register(r'oldperson', user_views.Old_personViewSet)
router.register(r'employee', user_views.EmployeeViewSet)
router.register(r'volunteer', user_views.VolunteerViewSet)
router.register(r'event', user_views.EventViewSet)
router.register(r'sys', user_views.SysViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url("login/$", user_views.LoginView.as_view()),
    url("facenow/$", user_views.get_facenow.as_view()),
    url("face/$", user_views.get_face.as_view()),
    url("isfall/$", user_views.get_isfall.as_view()),
    url("isunknow/$", user_views.get_isunknow.as_view()),

]
# urlpatterns += router.urls