
import abc
from django.contrib.auth.models import User

class PaymentService(abc.ABC):
    """
    Abstract interface for the payment service (contract).
    """

    @abc.abstractmethod
    def paymentIsValid(self, user: User) -> bool:
        """
        Checks if payment was successful 
        """
        pass

class AuthenticationService(abc.ABC):
    """
    Abstract interface for the authentication service (contract).
    """

    @abc.abstractmethod
    def userAuthenticated(self, user: User) -> bool:
        """
        Checks if user authentication was successful 
        """
        pass