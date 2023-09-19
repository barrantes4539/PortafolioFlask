from flask import Flask
import os

app = Flask(__name__)
app.config.from_mapping(
    SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
)

from . import portfolio
app.register_blueprint(portfolio.bp)

if __name__ == "__main__":
    app.run()