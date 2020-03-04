from flask import Flask
from flask import render_template, request

app = Flask(__name__)
list_images = []


@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == "GET":
        return render_template("GalleryUpload.html", title="Галерея с загрузкой", list=list_images)
    elif request.method == "POST":
        image_new = request.files["file"]
        list_images.append(f'/static/image/{image_new.filename}')
        return render_template("GalleryUpload.html", title="Галерея с загрузкой", list=list_images)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
