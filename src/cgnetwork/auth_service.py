import jwt
from rest_framework.response import Response

from cgnetwork import settings
from users.models.common import CustomUser


def authenticate_request(request):
    """
    Authenticate the request using a JWT token in cookies.

    This function retrieves the JWT token from the request cookies, and verifies it. If the token is valid, it retrieves
    the corresponding user. If anything goes wrong (no token, expired token, or user not found), it returns an error
    response.

    Parameters:
    request (HttpRequest): The Django HTTP request object from which the JWT token is to be retrieved.

    Returns:
    user: The authenticated user, or None if authentication failed.
    response (Response): A Django HTTP Response object. If authentication was successful, this is None. If not, it is
                         an HTTP response indicating the error that occurred (401 for unauthenticated, 404 for user not
                         found).
    """
    token = request.COOKIES.get('jwt')
    if not token:
        return None, Response({'error': 'Unauthenticated'}, status=401)

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None, Response({'error': 'Unauthenticated'}, status=401)

    user = CustomUser.objects.filter(id=payload['id']).first()
    if not user:
        return None, Response({'error': 'User not found'}, status=404)

    return user, None
