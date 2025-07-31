import logging

# getting logger object
log_obj = logging.getLogger()

log_format = "%(asctime)s  - %(levelname)s - %(msg)s"

logging.basicConfig(filename="autolog.txt", filemode="w", format=log_format, level="DEBUG")
# log levels - info, debug, warning, error, critical

log_obj.info("Informational message - fyr")
log_obj.debug("Script flow/traces messages")
log_obj.warning("Warning messages")
log_obj.error("Basic level Error messages")
log_obj.critical("Critical error that needs to be addressed")


# ref: https://docs.python.org/3/howto/logging.html