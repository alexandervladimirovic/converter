from django.urls import path


from .views import index


app_name = 'exchance_app'


urlpatterns = [
    path('', index, name='index'),
]