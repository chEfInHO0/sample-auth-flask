import logging

logger = logging.getLogger("sqlErrorHandler")
logger.setLevel(logging.ERROR)

if not logger.handlers:
    file_handler = logging.FileHandler('./logs/sqlErrorHandler.log',encoding='utf-8')
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

class SqlErrorHandler:
    def __init__(self, error):
        self.error = error

    def errors(self):
        error_msg = str(getattr(self.error, "orig", ""))
        error_type = type(self.error).__name__

        mapping = [
            ("UNIQUE constraint", ("Duplicate entry",409)),
            ("Duplicate entry", ("Duplicate entry",409)),
            ("FOREIGN KEY", ("Invalid relationship",400)),
        ]
        message,code = next(
        ((msg,c) for err,(msg,c) in mapping if err in error_msg),
        ("Integrity error on database",500)
        )
        logger.error(f"[{code}] {error_type}: {error_msg}")
        return {
            "message": message,
            "type": error_type,
            "error": error_msg,
            "status_code": code
        }