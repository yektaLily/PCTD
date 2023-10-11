



def getLogger(loggerName,logFile=None):
	import logging
	import sys
	logger = logging.getLogger(loggerName)
	logger.setLevel(logging.DEBUG)
	if logFile:
		handler = logging.FileHandler(logFile)
	else:
		handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	return logger