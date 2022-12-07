FROM python:3.9
USER root
RUN apt-get update
RUN apt-get -y install nodejs
RUN apt-get -y install npm
RUN npm install -g @vue/cli
COPY ./frontend /code/frontend
WORKDIR /code/frontend
CMD ["npm", "run", "serve"]
