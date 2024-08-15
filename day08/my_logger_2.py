import logging
logging.basicConfig(filename='my_server_log2.log',datefmt='%Y-%m-%d %H:%M:%S',level=logging.ERROR)
logger =logging.getLogger('logfile')
logger.info("this is fine")
logger.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
logger.error('this is an error','fix it.')
logger.critical('this is critical', 'fix it')