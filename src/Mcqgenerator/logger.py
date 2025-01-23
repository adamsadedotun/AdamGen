import logging
import os
from datetime import datetime

# Create log file name with the current date
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

# Define the path to save the log file
log_path = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Full path of the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s")

# Example log message
logging.info('Logging setup complete.')
