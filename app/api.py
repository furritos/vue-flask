import os
import time

from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap
from werkzeug.contrib.cache import SimpleCache

APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, 'templates')
STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, 'static')

app = Flask("VueFlask", template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
Bootstrap(app)

cache = SimpleCache()


@app.route("/")
def page_index_view():
    return render_template('index.html')


@app.route("/one")
def page_one_view():
    return render_template('one.html')


@app.route("/two")
def page_two_view():
    return render_template('two.html')


@app.route("/api/one")
def one():
    o = cache.get("one")
    if not o:
        o = {"one": [k for k in range(10)]}
        cache.set("one", o, timeout=30)
    return jsonify(o)


@app.route("/api/two")
def two():
    return jsonify(
        {
            "two": [k for k in range(10, 20)]
        }
    )


@app.route("/healthz")
def healthz():
    return jsonify(
        {
            "flask": True,
            "global": True
        }
    )


@app.route("/api/ts")
def ts():
    return jsonify(
        {
            "now": time.time()
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
