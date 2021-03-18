import os

from flask import Flask, render_template
from data import db_session
from data.table1 import Table1

app = Flask(__name__)


@app.route("/")
def index1():
    db_sess = db_session.create_session()
    table1 = db_sess.query(Table1).all()
    return render_template("index.html", table1=table1)


def main():
    db_session.global_init("db/bl.db")
    app.run()


if __name__ == '__main__':
    main()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
