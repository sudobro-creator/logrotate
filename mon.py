import os
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

# Check if directory exists and has the correct permissions
log_dir = '/var/log/mon'
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    os.chmod(log_dir, 0o755)

mon = Flask(__name__)

# Configure logging
log_file = os.path.join(log_dir, 'mon.log')
handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
mon.logger.addHandler(handler)

@mon.route('/')
def home():
    mon.logger.debug('Home page accessed at DEBUG level')
    mon.logger.info('Home page accessed at INFO level')
    return "Stage Seven!"

if __name__ == '__main__':
    mon.run(debug=True, host='0.0.0.0')
