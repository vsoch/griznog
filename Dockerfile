FROM continuumio/miniconda3

# docker build -t vanessa/griznog .

WORKDIR /code
COPY . /code
RUN python setup.py install
ENTRYPOINT ["griznog"]
