from flask import Flask, render_template, request, redirect, jsonify
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests
from transformers import pipeline
from texts import *


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ArticleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(1024), nullable=False)
    summary = db.Column(db.String(130), nullable=True)
    """
    def __repr__(self):
        return f"Article(original article = {article}, summary = {summary})" """


# db.create_all()

text_to_summary = ''
output = ''


def abort_if_article_id_not_found(article_id):
    if article_id not in articles:
        return abort(404, message="Article not found")


def make_text_summary(text_to_summary) -> str:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    summary = summarizer(text_to_summary, max_length=130, min_length=30)

    return summary[0]['summary_text']


article_put_agrs = reqparse.RequestParser()
article_put_agrs.add_argument('content', type=str, help='Content')


def get_wiki_article(url):
    req_obj = requests.get(url)
    text = req_obj.text
    soup = BeautifulSoup(text)
    all_ps = soup.find_all("p")
    wiki_article = ''
    for p in all_ps:
        wiki_article += p.text
    return wiki_article if len(wiki_article) < 1024 else wiki_article[0:1023]


class Article(Resource):
    def get(self, article_id):
        abort_if_article_id_not_found(article_id)
        return jsonify({'original': articles[article_id]})

    def put(self, article_id):
        args = article_put_agrs.parse_args()
        articles[article_id] = args
        return articles[article_id]

    def delete(self, article_id):
        del articles[article_id]
        return '', 204


class Summary(Resource):
    def get(self, summary_id):
        if summaries[summary_id] == '':
            text_to_summary = articles[summary_id]
            summary = make_text_summary(text_to_summary)
            return jsonify({'summary': summary})
        else:
            return jsonify({'summary': summaries[summary_id]})

    def put(self, summary_id):
        args = article_put_agrs.parse_args()
        summaries[summary_id] = args
        return summaries[summary_id]

    def delete(self, summary_id):
        del summaries[summary_id]
        return '', 204


api.add_resource(Article, "/articles/<int:article_id>")
api.add_resource(Summary, "/summaries/<int:summary_id>")


@app.get("/articles")
def get_articles():
    return list(articles.keys())


@app.get("/summaries")
def get_summaries():
    return list(summaries.keys())


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['text_to_summary'] != '' and request.form['url_to_summary'] == '':
            text_to_summary = request.form.get('text_to_summary')
            summary = make_text_summary(text_to_summary)
        elif request.form['text_to_summary'] == '' and request.form['url_to_summary'] != '':
            print(request.form.get('url_to_summary'))
            text_to_summary = get_wiki_article(request.form.get('url_to_summary'))
            summary = make_text_summary(text_to_summary)
        else:
            text_to_summary = "tutaj else (oba wypelnione lub puste)"
            summary = make_text_summary(text_to_summary)
        return render_template('index.html', output=summary, text_to_summary=text_to_summary)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
