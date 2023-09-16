from django.urls import path
from .views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('forDoctor/',forDoctor,name='forDoctor'),
    path('forDesk/',forDesk,name='forDesk'),

]