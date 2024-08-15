import logging
logging.basicConfig(filename='my_server_log.log')

logger = logging.getLogger()
#print(dir(logger))
#print(logger.__getattribute__.__doc__)
logger.info("this is fine")
logger.warning("this may break")
logger.error("this is a error", "fix it")
logger.critical("this is a critical error","fix it asap")
