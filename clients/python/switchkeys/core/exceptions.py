"""
Global SwitchKeys exception and warning classes.
"""

# --------------------------------------------------------------------
# Exceptions

##
# Base class for all kinds of client-side errors.


from switchkeys.utils.logger import SwitchKeysLogger


class Error(Exception):
    """Base class for client errors."""

    __str__ = object.__str__


class ResponseError(Error):
    """Indicates a broken response package."""

    pass

class AuthenticationError(Error):
    """Indicates a missing authentication."""

    SwitchKeysLogger.get_logger().error("There are no tokens found in the config file, and none were specified when initializing an instance of the SwitchKeys client. Please ensure that tokens are provided either in the config file or passed during initialization.")


class FeatureNotEnabled(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
