# import logging
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
#
# handler = logging.FileHandler("log.txt")


# import logging
# import logging.handlers
# import datetime
#
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
#                                                        atTime=datetime.time(0, 0, 0, 0))
# rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#
# f_handler = logging.FileHandler('error.log')
# f_handler.setLevel(logging.ERROR)
# f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#
# logger.addHandler(console)
#
# logger.addHandler(rf_handler)
# logger.addHandler(f_handler)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")

import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
