class AchcatException(Exception):
    """base achat exception"""


class HistoryException(AchcatException):
    """sonic memory exception"""


class SonicAuthError(AchcatException):
    """chatsonic login error"""
