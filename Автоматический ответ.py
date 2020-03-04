from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def mission():
    title = "Почта"
    surname = "Watny"
    name = "Mark"
    education = "выше среднего"
    profession = "штурман марсохода"
    sex = "male"
    motivation = "Всегда мечтал застрять на Марсе!"
    ready = "True"
    return render_template("auto_answer.html", title=title,
                           surname=surname,
                           name=name,
                           education=education,
                           profession=profession,
                           sex=sex,
                           motivation=motivation,
                           ready=ready)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
