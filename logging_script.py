import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", filemode="w", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")
