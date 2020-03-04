import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

data = {}


@app.route("/member")
def PersonalCard():
    with open("templates/InformationTeam.json", "r") as file:
        data = json.load(file)
    numberUser = 0  # Номер человека из экипажа
    name = data["team"][numberUser]["name"]
    username = data["team"][numberUser]["username"]
    image = data["team"][numberUser]["photo"]
    profession = data["team"][numberUser]["specialty"]
    print(data["team"])
    return render_template("PersonalCard.html", title="Личная карточка", name=name,
                           username=username,
                           image=image,
                           profession=profession)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")