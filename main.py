from flask import Flask, render_template, request, redirect, jsonify
from flask_restful import Api, Resource, reqparse, abort
from transformers import pipeline
from texts import *

text_to_summary = ''
output = ''
app = Flask(__name__)
api = Api(app)


def abort_if_article_id_not_found(article_id):
    if article_id not in articles:
        return abort(404, message="Article not found")


def make_text_summary(text_to_summary) -> str:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    summary = summarizer(text_to_summary, max_length=130, min_length=30)

    return summary[0]['summary_text']


article_put_agrs = reqparse.RequestParser()
article_put_agrs.add_argument('content', type=str, help='Content')


class Article(Resource):
    def get(self, article_id):
        abort_if_article_id_not_found(article_id)
        return jsonify({'orginal': articles[article_id]}) 

    def put(self, article_id):
        args = article_put_agrs.parse_args()
        articles[article_id] = args
        return articles[article_id]


class Summary(Resource):
    def get(self, article_id):
        text_to_summary = articles[article_id]
        summary = make_text_summary(text_to_summary)
        return jsonify({'orginal': text_to_summary, 'summary': summary})


api.add_resource(Article, "/articles/<int:article_id>")
api.add_resource(Summary, "/summary/<int:article_id>")


@app.get("/articles")
def get_articles():
    return list(articles.keys())


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST': 
        text_to_summary = request.form.get('text_to_summary')
        summary = make_text_summary(text_to_summary)
        return render_template('index.html', output=summary, text_to_summary=text_to_summary)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
