FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
RUN python -m pip install mysqlclient
RUN apt update && apt install -y ffmpeg libsm6 libxext6
#RUN apt-get install -y python-dev graphviz libgraphviz-dev pkg-config 
RUN apt-get install -y python3-dev graphviz libgraphviz-dev pkg-config
RUN pip install pygraphviz
RUN apt-get clean
COPY . /code/