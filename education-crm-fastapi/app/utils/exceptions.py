from fastapi import HTTPException, status


class UnauthorizedException(HTTPException):

    def __init__(self, detail="Invalid credentials"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail
        )


class NotFoundException(HTTPException):

    def __init__(self, detail="Resource not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )


class BadRequestException(HTTPException):

    def __init__(self, detail="Bad request"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )