import os
from flask import Flask, render_template, request, redirect, jsonify
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests
from summarizer import summarize


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'articles.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ArticleM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(1024), nullable=False)
    summary = db.Column(db.String(130), nullable=True)

    def __init__(self, article, summary):
        self.article = article
        self.summary = summary

    def __repr__(self):
        return f"article {self.id}: {self.article}, summary: {self.summary}"


"""with app.app_context():  # check for wether it already exists
    db.create_all() """
db.init_app(app)
with app.app_context():
    db.create_all()

text_to_summary = ''
output = ''

articles = []
summaries = []
art_ids = []

#for obj in db:
#    print(obj.article[0])


def abort_if_article_id_not_found(article_id):
    if article_id not in articles:
        return abort(404, message="Article not found")


def make_text_summary(text_to_summary) -> str:
    try: 
        summary=" ".join(summarize(text_to_summary[:10],text_to_summary))
    except:
        summary='There is a problem with creating summary '
    return summary


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
    return list(articles)


@app.get("/summaries")
def get_summaries():
    return list(summaries)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST' and (request.form['text_to_summary'] != '' or request.form['url_to_summary'] != ''):
        text_to = ''
        if request.form['text_to_summary'] != '' and request.form['url_to_summary'] == '':
            text_to = request.form.get('text_to_summary')
        elif request.form['text_to_summary'] == '' and request.form['url_to_summary'] != '':
            text_to = get_wiki_article(request.form.get('url_to_summary'))
        summary = make_text_summary(text_to)
        a = ArticleM(article=text_to, summary=summary)
        db.session.add(a)
        db.session.commit()
        if not art_ids:
            art_id = 0
        else:
            art_id = max(art_ids)+1
        art_ids.append(art_id)
        articles.append(text_to)
        summaries.append(summary)
        #api.add_resource(Summary, "/summaries/<int:summary_id>")
        return render_template('index.html', output=summary, text_to_summary=text_to, article_id=art_id)
    else:
        return render_template('index.html')


@app.route("/view")
def specify():
    return f"please specify full view number in the link as in view/number"


@app.route("/view/<int:art_id>")
def get_full(art_id):
    return jsonify({'article id': art_ids[art_id], 'original text': articles[art_id], 'summary': summaries[art_id]})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
