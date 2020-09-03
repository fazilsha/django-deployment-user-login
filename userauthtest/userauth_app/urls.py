from django.conf.urls import url
from userauth_app import urls
from userauth_app import views

#template urls!1

app_name = 'webpage'

urlpatterns=[
    url(r'^register/$',views.register,name="registration"),
    url(r'^user_login/$',views.user_login,name="user_login"),
]
