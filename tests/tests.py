import pytest

from main import abort_if_article_id_not_found


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def read_article(article_id):
    return article_id == 1


def article_answer():
    assert read_article(1) == """REST Architecture
REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.

REST defines the following architectural constraints:

Stateless: The server won’t maintain any state between requests from the client.
Client-server: The client and server must be decoupled from each other, allowing each to develop independently.
Cacheable: The data retrieved from the server should be cacheable either by the client or by the server.
Uniform interface: The server will provide a uniform interface for accessing resources without defining their representation.
Layered system: The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.
Code on demand (optional): The server may transfer code to the client that it can run, such as JavaScript for a single-page application.
Note, REST is not a specification but a set of guidelines on how to architect a network-connected software system.

Remove ads
REST APIs and Web Services
A REST web service is any web service that adheres to REST architecture constraints. These web services expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs.

For example, here’s one of the URLs for GitHub’s REST API:

https://api.github.com/users/<username>
This URL allows you to access information about a specific GitHub user. You access data from a REST API by sending an HTTP request to a specific URL and processing the response.

HTTP Methods
REST APIs listen for HTTP methods like GET, POST, and DELETE to know which operations to perform on the web service’s resources. A resource is any data available in the web service that can be accessed and manipulated with HTTP requests to the REST API. The HTTP method tells the API which action to perform on the resource.

While there are many HTTP methods, the five methods listed below are the most commonly used with REST APIs:"""


def article_id_not_found(article_id):
    return article_id == -1


def article_not_found_answer():
    return abort_if_article_id_not_found(-1)

