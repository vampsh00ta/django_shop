# syntax=docker/dockerfile:1

FROM python:3

RUN mkdir /site
COPY . /site
WORKDIR /site

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENTRYPOINT ["python","main.py"]
EXPOSE 3000
CMD ["python", "main.py"]
CMD ["export","FLASK_APP=main"]
CMD ["flask","run","-p","3000"]





