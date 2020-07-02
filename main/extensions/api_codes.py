from enum import Enum


class APICode(str, Enum):
    """
    API codes and descriptions

    Basic format `SA{xxx}{D|E|S}`:
        - Prefixes:
            - `SA` stands for `Seller API`
        - Suffixes:
            - `D`: Default suffix
            - `E`: Error cases
            - `S`: Success cases
    """

    def __new__(cls, value, description):
        obj = str.__new__(cls, value)
        obj._value_ = value

        obj.description = description
        return obj

    DEFAULT = ('SA001D', 'API has no specific code for this case')

    # Success codes
    GET_SUCCESS = ("SA001S", 'Success')
    CREATE_SUCCESS = ("SA002S", 'Created successfully!')
    DELETE_SUCCESS = ("SA003S", 'Deleted successfully!')
    UPDATE_SUCCESS = ("SA004S", 'Updated successfully!')

    # Errors codes
    UNHANDLED_ERROR = ("SA001E", "This error has not been handled")

    SELLER_NOT_FOUND = ("SA002E", "The requested seller can not be found")

    EXTERNAL_API_TIMEOUT = ("SA003E", "Got timeout when calling external API")

    PHYSICAL_VALIDATOR_ERROR = ("SA004E", "The requested params did not pass physical validation")

    LOGICAL_VALIDATOR_ERROR = ("SA005E", "The requested params did not pass logical validation")

    TOKEN_EXPIRED = ("SA051E", "Token expired")

    TOKEN_REQUIRED = ("SA052E", "Token required")

    TOKEN_ERROR = ("SA053E", "Token error")

    WRONG_LOGIN_INFO = ("SA054E", "Wrong login information")

    USER_INACTIVE = ("SA055E", "User inactive")

    ERROR_LOGIN_SOCIAL = ("SA056E", "Error login social")

    NOT_HAVE_PERMISSION = ("SA057E", "Not have permissions")
