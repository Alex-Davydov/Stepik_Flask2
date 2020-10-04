from flask import Flask, render_template

import data

app = Flask(__name__)


@app.route('/')
def main_view():
    return render_template('index.html', data=data)


@app.route('/departures/<string:departure>')
def departure_view(departure):
    return render_template('departure.html', data=data, departure=departure)


@app.route('/tours/<int:idn>/')
def tour_view(idn):
    return render_template('tour.html', data=data, id=idn)


if __name__ == '__main__':
    app.run()
