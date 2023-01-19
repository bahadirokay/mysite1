from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("index/", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("basic_table/", views.basic_table, name="basic_table"),
    path("blank/", views.blank, name="blank"),
    path("buttons/", views.buttons, name="buttons"),
    path("calendar/", views.calendar, name="calendar"),
    path("chartjs/", views.chartjs, name="chartjs"),
    path("form_component/", views.form_component, name="component"),
    path("gallery/", views.gallery, name="gallery"),
    path("lock_screen/", views.lock_screen, name="lock_screen"),
    path("login/", views.login, name="login"),
    path("morris/", views.morris, name="morris"),
    path("panels/", views.panels, name="panels"),
    path("responsive_table", views.responsive_Table, name="responsive_table"),
    path("todo_list", views.todo_list, name="todo_list"),
    path("general", views.general, name="general"),
    path("delete/<list_todo_id>", views.delete, name="delete"),
    path("update/<list_todo_id>", views.update, name="update"),
    path("yesfinished/<list_todo_id>", views.yesfinished, name="yesfinished"),
    path("nofinished/<list_todo_id>", views.nofinished, name="nofinished"),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
