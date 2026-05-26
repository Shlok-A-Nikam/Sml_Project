import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log_file = os.path.join(os.getcwd(), LOG_FILE)
os.makedirs(os.path.dirname(log_file), exist_ok=True)

logging.basicConfig(
    filename=log_file,
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("Detailed diagnostic information.")
logging.info("Confirmation that things are working.")
logging.warning("An unexpected issue occurred.")
 
# Expose a `logger` symbol for modules that import `from src.logger import logger`
logger = logging