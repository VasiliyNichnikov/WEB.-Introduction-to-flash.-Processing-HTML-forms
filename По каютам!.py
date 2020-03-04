from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/distribution")
def mission():
    distribution = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template("cabin.html", title="По каютам!", distribution=distribution)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
