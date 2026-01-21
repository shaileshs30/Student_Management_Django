
from django.urls import path
from. import views
urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.user_signup,name='signup'),
    path("", views.student_list, name='student_list'),
    path("add/",views.student_create,name='student_create'),
    path("edit/<int:id>/",views.student_update,name='student_update'),
    path("delete/<int:id>/",views.student_delete,name='student_delete'),
    path("profile/<int:id>",views.student_profile,name='student_profile'),
    path("detail/<int:id>/",views.student_detail,name='student_detail'),
]