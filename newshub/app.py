from flask import Flask, render_template
from models import Daily, News, app, db
from scraper import *
from flask_apscheduler import APScheduler



scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@scheduler.task('interval', id='do_job_1', hours=3, misfire_grace_time=900)
def job1():
    get_all()
    print('Database Updated')

@app.route('/')
def home():  # put application's code here

    daily = Daily.query.all()
    news = News
    return render_template("home.html",daily = daily, news = news)

@app.route('/<int:daily_id>')
def daily(daily_id):  # put application's code here

    daily = Daily.query.get_or_404(daily_id)
    news = News
    return render_template("daily.html",i = daily, news = news)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
