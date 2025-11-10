import logging
def get_logger(name: str = __name__):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger(name)
logger = get_logger("app")
logger.info("Logging made simple!")
