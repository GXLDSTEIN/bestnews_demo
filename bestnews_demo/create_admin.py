from getpass import getpass
import sys

from bestnews_demo import create_app
from .model import User, db

app = create_app()

with app.app_context():
    username = input('Enter user name: ')

    if User.query.filter(User.username == username).count():
        print('User already exists')
        sys.exit(0)

    password = getpass('Enter password: ')
    password2 = getpass('Repeat password: ')
    if not password == password2:
        sys.exit(0)
    new_user = User(username=username, is_admin=True)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))