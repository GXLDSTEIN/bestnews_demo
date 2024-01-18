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

    max_attempts = 3
    for attempt in range(max_attempts):
        password = getpass('Enter password: ')
        password2 = getpass('Repeat password: ')
        if password == password2:
            break
        else:
            print(f'Passwords do not match. Please try again.')

    if not password == password2:
        print(f'Exceeded maximum attempts ({max_attempts})')
        sys.exit(0)
        
    new_user = User(username=username, is_admin=True)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f'User with id {new_user.id} and username {new_user.username} added')