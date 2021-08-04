import logging
import logging.config
import os

import otherMod2


def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """
    dictLogConfig = {
        "version": 1,
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": "config2.log"
            }
        },
        "loggers": {
            "exampleApp": {
                "handlers": ["fileHandler"],
                "level": "INFO"
            }
        }
    }

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("exampleApp")
    logger.info("Program started")
    result = otherMod2.add(7, 8)
    logger.info("Done!")


if __name__ == "__main__":
    os.remove(os.path.join("config2.log"))
    main()
