from flask import (
    Flask,
    request,
    render_template,
    url_for,
    render_template_string,
    make_response,
)


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/users")
def users():
    html = """<html><body>
    <h1>Hello!</h1>
    <h3>Enter user name in browser "/user/user_name"</h3>
    </body></html>"""
    return render_template_string(html)
    # return 'Enter user name in browser "/user/user_name"'


users = []


@app.route("/users/<user>")
def add_users(user):
    users.append(user)

    return render_template("users.html", users=users)


@app.route("/set_cookies", methods=["GET"])
def cookie():

    return render_template("form.html")


@app.route("/cookies", methods=["GET"])
def set_cookie():
    name_lang = request.args["lang"]
    name_user = request.args["username"]
    response = make_response(render_template("cookies.html"))
    response.set_cookie("USERNAME", name_user)
    response.set_cookie("LANG", name_lang)

    return response


@app.route("/get_cookies", methods=["GET"])
def get_cookie():
    html_lang = request.cookies.get("LANG")
    html_user = request.cookies.get("USERNAME")
    return "<h1> Lang:" + html_lang + "</h1>" "<h1> User:" + html_user + "</h1>"


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
    )
