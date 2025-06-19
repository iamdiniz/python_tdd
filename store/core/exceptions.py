class BaseException(Exception):
    message: str = "Inteernal Server Error"

    def init__(self, message: str | None = None) -> None:

        if message:
            self.message = message

    
class NotFoundException(BaseException):
    message = "Not Found"