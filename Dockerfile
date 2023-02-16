FROM python:3.9
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD garden.py /app/nlp.py