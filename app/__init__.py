from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

    from . import portfolio
    app.register_blueprint(portfolio.bp)

    return app

if __name__ == "__init__":
    app = create_app()
    app.run()