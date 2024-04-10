from flask import Flask, request, render_template, url_for, render_template_string


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


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
    )
