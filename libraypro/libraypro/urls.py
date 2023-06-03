"""
URL configuration for libraypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings 
from django.conf.urls.static import static 


from django.contrib import admin
from django.urls import path,include
from libapp import views
urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('login/',views.user_login1,name='login1'),
    path('logout/',views.user_logout1,name='logout1'),
    path('membership/',views.register,name='member'),
    path('signup/',views.signup1,name='signup1'),
    path('contact/',views.contact,name='contact'),
]
    
#     path('blog/<int:id>',views.blog_view,name='blog'),
#     # path('delete/<int:p>',views.delete_emp,name='delete_emp'),
#     # path('edit/<int:p>',views.edit_emp,name='edit_emp'),
#     # path('view_data/<int:p>',views.data,name='data'),
#     path('details/<int:id>/', views.detail_view, name='detail')
# ]
# if(settings.DEBUG):
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

