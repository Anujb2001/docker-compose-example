# NOTE name need to be Dockerfile
FROM python:3.9

# RUN pip install mysql-connector-python
# RUN pip install flask_sqlalchemy

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app.py ./
CMD ["python", "app.py"]