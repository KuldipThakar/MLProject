import logging
import os
from datetime import datetime

# Generate a log file name based on current datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Make sure the 'logs' directory exists
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setup logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] - %(lineno)d -name %(name)s - %(filename)s - Line: %(levelname)s - Message: %(message)s",
    level=logging.INFO,
)

