FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add musl-dev mariadb-dev gcc
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# COPY --from=base /usr/share/zoneinfo /usr/share/zoneinfo
# ENV TZ: America/Monterrey

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000