from flask.cli import FlaskGroup
import unittest
from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    """
        Spins Up DB Instance
    """
    
    with app.app_context():
        db.drop_all()   
        db.create_all()
        db.session.commit()

@cli.command('test')
def test():
    """
        Runs All Tests
    """
    #print(app.config, file=sys.stderr)
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='mercy', email="mercy@gmail.com"))
    db.session.add(User(username='bolum', email="bolum@gmail.com"))
    db.session.commit()


if __name__== '__main__':
    cli()