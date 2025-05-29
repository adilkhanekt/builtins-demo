import logging


# # It is not recommended to call logging registrators directly, like this:
# logging.debug("Debug message")
# logging.info("Infromation about event")
# logging.warning("Warning message")
# logging.error("Error message")
# logging.critical("Critical error")


# Instead we should set logging level and then get logging registrator by using getLogger method

# logging.basicConfig(level=logging.NOTSET)
# logging.basicConfig(filename="full1.log", level=logging.NOTSET, encoding="utf-8")
# logger = logging.getLogger(__name__)


FORMAT = "{levelname} - {asctime} - {msg}"

logging.basicConfig(filename="full2.log", level=logging.NOTSET, encoding="utf-8", format=FORMAT, style="{")
logger = logging.getLogger(__name__)


# logger.debug("Debug message")
# logger.info("Infromation about event")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical error")


def division_of_two_numbers(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as e:
        logger.error(f"Error of divions {n1} / {n2}: {e}")
        return


division_of_two_numbers(3, 0)



# Logging levels
#
# logging.NOTSET        0              # no functional behavior, serves as a fallback when no level is specified
# logging.DEBUG         10             # used to log detailed diagnostic and debugging messages that help developers troubleshoot their code
# logging.info          20             # used to log general information about the application’s execution flow or significant application events
# logging.WARNING       30    Default  # used to warn about potential issues that could disrupt execution later but aren't breaking the application now
# logging.ERROR         40             # logs significant issues that prevent some part of the app functionality, but do not crash the entire app
# logging.CRITICAL      50             # used to indicate severe errors that may cause the application to crash or terminate