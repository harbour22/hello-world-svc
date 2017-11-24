FROM python:alpine
EXPOSE 8080
ADD . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
CMD python helloworldservice.py
