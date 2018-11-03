from server import app
from flask import send_from_directory

@app.route('/')
def root():
    return send_from_directory('../templates', 'index.html')