import logging
import time

# create a logger
logger = logging.getLogger(__name__)
# set the log level
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('my_log.txt')
# set the log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handler to the logger
logger.addHandler(handler)
# log a message
while True:
   logger.info('This is a message')
   time.sleep(5)
