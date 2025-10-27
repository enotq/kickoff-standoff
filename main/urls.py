from django.urls import path
from main.views import (show_main, add_product, view_product, show_xml, show_json, show_json_by_id, show_xml_by_id,
                        register, login_user, logout_user, edit_product, delete_product) #add_car

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('view-product/<str:id>/', view_product, name='view_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('view-product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('view-product/<uuid:id>/delete', delete_product, name='delete_product'),
    #path('car/new', add_car, name='add_car')
]