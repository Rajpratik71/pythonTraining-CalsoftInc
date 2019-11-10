"""
Module to demonstrate how to create simple we application using aiohttp.
"""

from aiohttp import web

routes = web.RouteTableDef()

# ==================A SIMPLE WEB APPLICATION USING AIOHTTP ======================


@routes.get("/")
async def home(request):
    """
    Args:
        request: HTTP request object

    Returns:
        http response
    """
    return web.Response(text="Welcome to aiohttp")


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)

# ==============A SIMPLE WEB APPLICATION USING AIOHTTP API/FEATURES ================


# @routes.get("/")
# async def home(request):
#     """
#     Args:
#         request: HTTP request object
#
#     raises:
#         HTTPFound to redirect request to new url
#     """
#     welcome_location = (
#         request.app.router["welcome"]
#         .url_for(name="to aiohttp")
#         .with_query({"query": "how are you"})
#     )
#     raise web.HTTPFound(location=welcome_location)
#
#
# @routes.get("/welcome/{name}", name="welcome")
# def welcome(request):
#     """
#     Args:
#         request: HTTP request object
#
#     Returns:
#         http response
#     """
#     name = request.match_info["name"]
#     if name == "guest":
#         raise web.HTTPUnauthorized()
#     return web.Response(text="Welcome %s" % name)
#
#
# if __name__ == "__main__":
#     app = web.Application()
#     app.add_routes(routes)
#     web.run_app(app)
