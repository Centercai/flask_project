from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import db, create_app

app = create_app("development")
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route("/")
def index():
    return "hello world 世界真美好"


if __name__ == '__main__':
    manager.run()
