from django.urls import path

from . import views

app_name='todoapp'
urlpatterns=[
    path('',views.veiw_tasks,name='view_tasks'),
    path('add',views.add_task,name='add_task'),
    path('edit',views.edit_task,name='edit_task'),
    path('delete',views.delete_task,name='delete_task')

]
