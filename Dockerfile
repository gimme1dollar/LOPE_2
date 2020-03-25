FROM nikolaik/python-nodejs
ENV PYTHONUNBUFFERED 1

RUN mkdir /web
WORKDIR /web
COPY requirements.txt /web/
RUN pip install -r requirements.txt
COPY . /web/
RUN npm install
RUN npm run build
