# Book-store
This example shows how to work with book store. <br />

Quick start
-----------------
1. ``git clone https://github.com/YevgeniiKaidashov/book-store.git``
2. Go to project root folder in the terminal and execute command ``pip install -r requirements.txt``
3. Execute command ``manage.py migrate`` to apply all migrations and create db.sqlite3 by default
4. Execute command ``manage.py loaddata author.json`` to load authors data to database from fixtures
4. Execute command ``manage.py loaddata book.json`` to load books data to database from fixtures
5. Execute command ``manage.py createsuperuser`` to create a superuser account, which we can use for admin panel
6. There is ``manage.py show_books`` command. <br />
By default it shows books by ASC ordering, if you want to order by DESC use ``--order desc`` argument
