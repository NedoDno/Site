from data import db_session

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    app.run()


@app.route('/')
def index():
    return 'Мам, дай денег'



if __name__ == '__main__':
    main()
