FROM python:3.7
LABEL maintainer="info@devs-group.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./entrypoint.sh /usr/local/bin

WORKDIR /app
COPY ./ /app

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/usr/local/bin/entrypoint.sh"]
