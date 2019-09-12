FROM node:8.16.1-alpine
MAINTAINER Amit Thapa <amithapa1994@gmail.com>

WORKDIR /app

ADD src /app/src
ADD package.json /app/

RUN yarn install && yarn run build && yarn install --production=true
RUN rm -rf src && rm -rf package.json

EXPOSE 4000

CMD ["node","/app/dist/server.js"]