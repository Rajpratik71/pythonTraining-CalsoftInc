def authenticator(func):
    def wrapper(request):
        if request["name"] == "Calsoft":
            func(request)
        else:
            print("You are not authorized")

    return wrapper


@authenticator
def api(request):
    print("performing some operations as the request has been authenticated")


request = {"name": "NetApp"}
api(request)
