from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app, db

# handles all db migrations thru Flask-Migrate
migrate = Migrate(app, db)

# exposes all db migration thru Flask-Script
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()