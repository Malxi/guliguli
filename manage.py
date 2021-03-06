#!venv/bin/python

import os
from app import create_app
#from app.models import User, Role
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))

#@manager.command
#def test():
#    """Run the unit tests."""
#    import unittest
#    tests = unittest.TestLoader().discover('tests')
#    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
    #app.run(debug=True, host="0.0.0.0", port=80)
