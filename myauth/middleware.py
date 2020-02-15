from myauth.models import AuthSession


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        try:
            myHash = request.COOKIES.get('myhash')
            userId = AuthSession.objects.get(hash=myHash)
            request.myUserId = userId.myuserId
            print('-----------------------middleware------------------------')
            print(userId.myuserId )
            print('-----------------------middleware------------------------')
        except:
            request.myUserId = None
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response