class ApiError(Exception):
    def __init__(self, error_code, error_msg):
        self.error_code = error_code
        self.error_msg = error_msg
        super().__init__(f"API Error [{error_code}]: {error_msg}")

class ApplicationError(ApiError):
    pass

class HttpError(ApiError):
    pass

class NoOpenApiServiceError(ApiError):
    pass

class ServiceAccessDeniedError(ApiError):
    pass

class LimitedNumberOfServiceRequestsExceedsError(ApiError):
    pass

class ServiceKeyNotRegisteredError(ApiError):
    pass

class DeadlineHasExpiredError(ApiError):
    pass

class UnregisteredIpError(ApiError):
    pass

class UnknownError(ApiError):
    pass
