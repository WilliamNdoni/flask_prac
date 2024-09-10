import sqlite3

import click
from flask import current_app,g

# Connecting to the database
def get_db():

    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# Closing the connection to the database
def close_db(e=None):
    db = g.pop('db',None)

    if db is not None:
        db.close()
# Connecting to the database and executing the database schema
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Creating a CLI command to initialize the database
@click.command('initializedb')
def init_db_cli():
    init_db()
    click.echo('Database initialized')

def init_app(app):
    # Closing the database after the response is returned
    app.teardown_appcontext(close_db)
    # Adding the cli command to flask
    app.cli.add_command(init_db_cli)
