#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Run migrations (optional, but often needed)
python manage.py migrate

# Start the Django server
python manage.py runserver 0.0.0.0:$PORT
