FROM python:3.11.3-alpine3.16
RUN mkdir -p /home/app
COPY ./app/ /home/app
WORKDIR /home/app/
RUN pip install -r requirements.txt
#CMD ["python", "app.py"]
CMD ["flask", "run", "--host", "0.0.0.0"]