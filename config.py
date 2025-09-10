import os

# SECURITY: Use a strong random value in production, otherwise retrieve from environment variable
SECRET_KEY = os.environ.get("SECRET_KEY", "dummy-secret-key")

# Maximum allowed payload to 4MB to prevent DoS attacks
MAX_CONTENT_LENGTH = 4 * 1024 * 1024

# SQLAlchemy configuration
# SQLALCHEMY_DATABASE_URI will be set dynamically in create_app() using app.instance_path
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Upload configuration
# Files are stored in the instance/uploads directory
UPLOAD_FOLDER = "uploads"
