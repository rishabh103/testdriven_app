from flask.cli import FlaskGroup
from project import create_app, db
import unittest
from project.api.models import User
import coverage

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
    'project/tests/*',
    'project/config.py',
    ]
)
COV.start()


app = create_app()
cli = FlaskGroup(create_app=create_app)
print(cli)

@cli.command()
def recreate():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return 1

@cli.command()
def test():
    """ Runs the tests without code coverage"""
    test = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    print(test,flush=True)
    result = unittest.TextTestRunner(verbosity=2).run(test)
    if result.wasSuccessful():
        return 0
    return 1
    # print("LOL")
    
@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()