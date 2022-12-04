import pytest

from flask_restful import abort

articles = {0: """New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.""", 1: """REST Architecture
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

While there are many HTTP methods, the five methods listed below are the most commonly used with REST APIs:""", 2: """What NLP Can Do
The best known natural language processing tool is GPT-3, from OpenAI, which uses AI and statistics to predict the next word in a sentence based on the preceding words. NLP practitioners call tools like this “language models,” and they can be used for simple analytics tasks, such as classifying documents and analyzing the sentiment in blocks of text, as well as more advanced tasks, such as answering questions and summarizing reports. Language models are already reshaping traditional text analytics, but GPT-3 was an especially pivotal language model because, at 10x larger than any previous model upon release, it was the first large language model, which enabled it to perform even more advanced tasks like programming and solving high school–level math problems. The latest version, called InstructGPT, has been fine-tuned by humans to generate responses that are much better aligned with human values and user intentions, and Google’s latest model shows further impressive breakthroughs on language and reasoning.

For businesses, the three areas where GPT-3 has appeared most promising are writing, coding, and discipline-specific reasoning. OpenAI, the Microsoft-funded creator of GPT-3, has developed a GPT-3-based language model intended to act as an assistant for programmers by generating code from natural language input. This tool, Codex, is already powering products like Copilot for Microsoft’s subsidiary GitHub and is capable of creating a basic video game simply by typing instructions. This transformative capability was already expected to change the nature of how programmers do their jobs, but models continue to improve — the latest from Google’s DeepMind AI lab, for example, demonstrates the critical thinking and logic skills necessary to outperform most humans in programming competitions.

Models like GPT-3 are considered to be foundation models — an emerging AI research area — which also work for other types of data such as images and video. Foundation models can even be trained on multiple forms of data at the same time, like OpenAI’s DALL·E 2, which is trained on language and images to generate high-resolution renderings of imaginary scenes or objects simply from text prompts. Due to their potential to transform the nature of cognitive work, economists expect that foundation models may affect every part of the economy and could lead to increases in economic growth similar to the industrial revolution."""}


def inc(x):
    return x + 1


def read_article(article_id):
    return articles[article_id]


def article_id_not_found(a_id):
    return a_id not in articles.keys()


def test_answer():
    assert inc(4) == 5
    assert read_article(1) == articles[1]
    assert True if article_id_not_found(-1) else False


# test_answer()  #  uncomment this code to test locally
