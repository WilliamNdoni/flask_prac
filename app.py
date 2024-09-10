import os
from flask import Flask,render_template
# Creating an application factory for the CRUD application
def create_app(test_config=None):
    #creating and configuring the app
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='wuzu',
        DATABASE= os.path.join(app.instance_path,'crud.sqlite')
    )
    if test_config is None:
        #Loading the instance config when not testing,if it exists
        app.config.from_pyfile('config.py',silent=True)
    else:
        #Loading the test config if parameter passed
        app.config.from_mapping(test_config)
    #Ensuring that the instance folder exists otherwise it is created
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Creating a simple page
    @app.route('/hello')
    def hello():
        return 'Hello, world'
    
    
    import database
    database.init_app(app)

    import auth
    app.register_blueprint(auth.bp)

    import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index')


    return app