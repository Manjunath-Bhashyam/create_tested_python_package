import os
import logging
import sys

logger_str = "[%(asctime)s:%(levelname)s:%(module)s]: %(message)s"
log_dir = "./logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logger_str,
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(log_filepath)],
)

logger = logging.getLogger("IPYNBrenderer")
