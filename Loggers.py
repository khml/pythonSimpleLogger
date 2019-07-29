# coding:utf-8

from logging import Logger, getLogger, DEBUG, INFO, WARNING, ERROR, StreamHandler, FileHandler, Formatter


def get_io_stream_logger(name: str, log_level: object = DEBUG,
                         add_stream: bool = True,
                         filename: str = None,
                         format_str: str = "%(asctime)s - %(levelname)s - %(message)s") -> Logger:
    """
    :param name:
    :param log_level: logging.DEBUG, logging.INFO, and etc.
    :param add_stream:
    :param filename: str
    :param format_str:
    :return: Logger
    """
    logger = getLogger(name)
    logger.setLevel(log_level)

    formatter = Formatter(format_str)

    if add_stream:
        stream_handler = StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    if filename is not None:
        file_handler = FileHandler(filename)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(format_str)
        logger.addHandler(file_handler)

    return logger
