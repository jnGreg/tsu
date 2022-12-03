import pytest

from flask_restful import abort

import texts
from texts import articles


def inc(x):
    return x + 1


def read_article(article_id):
    return texts.articles[article_id]


def article_id_not_found(article_id):
    return article_id == -1


def test_answer():
    assert inc(4) == 5
    assert read_article(1) == texts.articles[1]
    assert article_id_not_found(-1) == abort(404, message="Article not found")
