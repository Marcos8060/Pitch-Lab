from app import app
from  flask_migrate import Migrate, MigrateCommand
from app import app,db
from app.models import User,Pitch
from flask_script import Manager,Server


manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User=User, Pitch = Pitch)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()

if __name__== '__main__':
    app.run(debug=True)