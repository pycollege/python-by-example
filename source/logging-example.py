import logging

# Basic config
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.debug("This won't show (level too low)")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
