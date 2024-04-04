from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/age/<int:age>")
def check(age):
    if age < 18:
        return "Вы несовершеннолетний!"
    else:
        return "Доступ получен!"


@app.route("/users/<int:id_user>/<username>")
def answer(username, id_user):
    return f"Ник: {username}, ID: {id_user}"


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
    )
