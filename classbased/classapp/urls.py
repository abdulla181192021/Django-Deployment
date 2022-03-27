from django.urls import path
from classapp import views

app_name='classapp'
urlpatterns=[
path('index/',views.index,name='index'),
path('indexview/',views.Indexview.as_view(),name='indexview'),
path('',views.Templatesview.as_view(),name='templateview'),
path('listview/',views.Listviews.as_view(),name='listview'),
path('musician_detail/<pk>',views.Musician_detail.as_view(),name='musician_detail'),
path('addmusician/',views.AddMusician.as_view(),name='add_musician'),
path('musician_update/<pk>/',views.UpdateMusician.as_view(),name='musician_update'),
path('musician_delete/<pk>/',views.DeletMusician.as_view(),name='musician_delete'),


]
