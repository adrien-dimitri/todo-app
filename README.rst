=====
To-Do App
=====

To-Do App is a Django app to create and manage tasks to be done. Each user has their own tasks and can create, read, update and delete them.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "todo.apps.TodoConfig" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'todo.apps.TodoConfig',
    ]

2. Add "LOGIN_URL = 'todo:login'" to your settings.py to configure the login url.

3. Include the todo app URLconf in your project urls.py like this::

    urlpatterns = [
        path('todo/', include('todo.urls')),
        path('admin/', admin.site.urls),
    ]

4. Run ``python manage.py migrate`` to create the Task models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a user and login to use the app.

6. Visit http://127.0.0.1:8000/todo/ and login to use the To-Do App.