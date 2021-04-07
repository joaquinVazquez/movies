from flask import Flask

import views
from database import Database


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/movies", view_func=views.movies_page)
    app.add_url_rule("/movies", view_func=views.movies_page, methods=["GET", "POST"])
    app.add_url_rule("/movies/<int:movie_key>", view_func=views.movie_page)
    app.add_url_rule("/new-movie", view_func=views.movie_add_page, methods=["GET", "POST"])

    db = Database()
    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    # port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=8080)
