FROM alpine:3.17

RUN apk update && apk upgrade\
    && apk add --no-cache python3 py3-pip

# FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 23465

CMD ["gunicorn", "--bind", "0.0.0.0:23465", "wsgi:application"]