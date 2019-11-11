"""
Module to demonstrate how to create simple we application using flask.
"""

from flask import Flask, redirect, url_for, abort, request, render_template

# app = Flask(__name__)

# ==================A SIMPLE WEB APPLICATION USING FLASK ======================


# @app.route("/")
# def home():
#     """
#     Returns:
#         welcome message
#     """
#     return "Welcome to Flask"
#
#
# if __name__ == "__main__":
#     app.run()


# ==============A SIMPLE WEB APPLICATION USING FLASK API/FEATURES ================

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    Returns:
        redirect request to new url
    """
    return redirect(url_for("welcome", name="to Flask", query="how are you"))


@app.route("/welcome/<name>")
def welcome(name):
    """
    Args:
        name (str): name from url path

    Returns:
        html template
    """
    if name == "guest":
        abort(401)
    print(request.args.get("query"))
    return render_template("welcome.html", username=name)


if __name__ == "__main__":
    app.add_url_rule("/", "welcome", welcome)
    app.debug = True
    app.run(host="0.0.0.0", port="8082", debug=True)
