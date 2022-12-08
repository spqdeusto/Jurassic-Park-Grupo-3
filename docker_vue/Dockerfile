FROM node:lts-alpine
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
RUN npm install -g @vue/cli
CMD ["npm", "run", "serve"]
