# txt_sum_up_proj

##  Project Description
A simple REST API app to summarize texts given in the form of a URL or pasted.<br>
Only wikipedia articles addressed by URL are being handled rather well at the current state of development. Feel free to experiment with other sources. We take no responsibility. <br>
Max text length is 1024 chars as of now. It works slow enough anyway, trust us.<br>

## Instruction
To run this locally, you can use the command if you have Docker installed.    

```bash
docker-compose up
```   
If you do not have Docker, you can install the required dependencies by running   
```bash
pip install -r requirements.txt
```   
and then start the application with  
```bash
python app.py
```


## Technologies
- [Python] - Web programming language, version 3.9
- [Flask] - Web App Framework
- [Fly.io] - Hosting platform
- [Docker] - Docker
- [REST API] - REST API

[//]:  # (These are reference links http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Python]: <https://www.python.org/>
   [Flask]: <https://flask.palletsprojects.com/en/2.2.x/>
   [Fly.io]: <https://fly.io>
   [Docker]: <https://www.docker.com/>
   [REST API]: <https://restfulapi.net/>

