from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
# instantiate the app
# app = Flask(__name__)
# print(os.getenv)
# app_settings = os.getenv('APP_SETTINGS')
# app.config.from_object(app_settings)

db = SQLAlchemy()
migrate = Migrate()
# print(app.config)
bcrypt = Bcrypt()
def create_app(script_info=None):
    
    app = Flask(__name__)
    CORS(app)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from project.api.users import users_blueprint

    app.register_blueprint(users_blueprint)

    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    app.shell_context_processor({'app': app, 'db': db})
    return app





# @app.route('/users/ping', methods=['GET'])
# def ping_pong():
#     # db.drop_all()
#     db.create_all()
#     db.session.commit()

#     return jsonify({
#     'status': 'success',
#     'message': 'pong!'
#     })

# @app.route('/test', methods=['GET'])
# def test_pong():
#     tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
#     # suite  = unittest.TestSuite(tests)
#     # tests._cleanup = False
#     print(tests,flush=True)
#     result = unittest.TextTestRunner(verbosity=2)
#     print(result, flush=True)
#     result = result.run(tests)
#     if result.wasSuccessful():
#         return jsonify({
#         'status': 'success',
#         'message': 'pong!'
#         })
#     # return 1
    
#     return jsonify({
#     'status': 'success',
#     'message': 'pong!'
#     })