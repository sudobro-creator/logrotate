# logrotate
This Flask application demonstrates how to configure logging with rotation using Python’s logging module and RotatingFileHandler. The application logs access to the home page and handles log rotation automatically, keeping up to 7 backup logs.

Prerequisites

    Python 3.x
    Flask (pip install flask)

Features

    Logging: Logs messages at both DEBUG and INFO levels.
    Log Rotation: Automatically rotates logs after reaching 1 MB in size, keeping up to 7 backup logs.
    Permissions: Ensures the log directory exists with appropriate permissions.

Setup

    Create the Log Directory:
        The application will automatically create the directory /var/log/mon if it does not exist.
        The directory permissions are set to 755 to allow read and execute access.

    Configure Logging:
        RotatingFileHandler is used to manage log rotation.
        Logs are stored in mon.log with a maximum size of 1 MB. Up to 7 backup logs are kept.




What is log rotation
In information technology, log rotation is an automated process used in system administration in which log files are compressed, moved (archived), renamed or deleted once they are too old or too big (there can be other metrics that can apply here).

Logrotate is mainly used to log, rotate and compress logs. If you are logging daily, it means that how many logs of daily copies do you want to keep

![image](https://github.com/user-attachments/assets/486babc0-b74d-492e-980d-b61179c5c141)
<p>The log rotation strategy involves managing the log file /var/log/wtmp to ensure efficient disk space usage and maintain a history of log entries. The log rotation is configured to occur monthly, with specific settings for file permissions, minimum size before rotation, and the number of backup copies.</p>

## Configuration Details
- Rotation Frequency:
  Logs are rotated on a monthly basis.

- File Permissions and Ownership:
  - Upon rotation, the new log file inherits permissions 0664, which allows read and write access for the owner and group, and read-only access for others.
  - The log files are owned by the root user and utmp group.

- File Size Before Rotation:
  - The log file is rotated when its size reaches 1 MB.

- Backup Copies:
  - Only one backup copy of the log file is maintained. This means that after rotation, the existing file will be renamed, and a new log file will be created.

## Log Rotation Directives

- `create` Directive:
  The create directive specifies that a new log file is created after rotation. For instance, the original log file named my.app will be rotated and renamed to my.app.1, and a new my.app file will be created for further logging.

- `copytruncate` Directive:
  The copytruncate directive allows for the existing log file to be copied and truncated. When this directive is used, the existing log file (my.app) is copied to my.app.1, and the original file (my.app) is emptied to continue logging without interruption.

# The Application Setup

## Import Statements
```
import os
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

```

## Directory Setup
```
log_dir = '/var/log/mon'
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    os.chmod(log_dir, 0o755)

```

## Flask Application Setup
```
mon = Flask(__name__)
```

## Logging Configuration
```
log_file = os.path.join(log_dir, 'mon.log')
handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
mon.logger.addHandler(handler)
```

## Route Definition
```
@mon.route('/')
def home():
    mon.logger.debug('Home page accessed at DEBUG level')
    mon.logger.info('Home page accessed at INFO level')
    return "Stage Seven!"
```

## To Run the application
```
if __name__ == '__main__':
    mon.run(debug=True, host='0.0.0.0')
```
<p>This allows you to access the application on any IP address that the host machine has.</p>



## Running the Application

To run the application, use:
```
python <your_script_name>.py
```
<p>The application will start a Flask server accessible from all network interfaces (0.0.0.0).<p>


## Accessing the Application
<p>Open your browser and navigate to `http://<server_ip>:5000/`. Access to this page will be logged.<p>

## Additional Notes
<p>
  - Ensure that the Flask application has the necessary permissions to write to the log directory.
  - Adjust maxBytes and backupCount according to your needs for log management.  
</p>

## Troubleshooting
<p>
  - Permission Issues: Ensure the directory /var/log/mon is writable by the Flask application.
  - Log File Rotation: If logs are not rotating as expected, check the maxBytes and backupCount settings.
  
</p>
