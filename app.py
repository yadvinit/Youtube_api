# Project structure:
# - app.py (main entry point)
# - config.py (configuration settings)
# - services/youtube_service.py (API interaction)
# - routes/main_routes.py (route handlers)
# - templates/home.html (HTML template)
# - .env (environment variables)

# app.py
from flask import Flask
from routes.main_routes import main_bp
from config import Config
# from services.db import mongo


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    #mongo.init_app(app)
    # Register blueprints
    # with app.app_context():
    #     mongo.db.videos.create_index("videoId", unique=True)
        
    app.register_blueprint(main_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)