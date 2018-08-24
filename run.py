"""
app root of the api endpoints
"""


from api.instances.config import DevelopmentConfig, ProductionConfig
from flask import Flask
from api.app.views import Links


class Server:
    """Create flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        Links.generate(app)
        return app


App = Server().create_app(config=DevelopmentConfig)


if __name__ == '__main__':
    App.run()
