FROM python:3.9
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD nlp.py /app/nlp.py