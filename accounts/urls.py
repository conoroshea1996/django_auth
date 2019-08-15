from django.conf.urls import url, include, re_path
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    re_path(r'^logout/', logout, name='logout'),
    re_path(r'^login/', login, name='login'),
    re_path(r'^register/', registration, name='registration'),
    re_path(r'^profile/', user_profile, name='profile'),
    re_path(r'^password-reset/', include(url_reset))
]
