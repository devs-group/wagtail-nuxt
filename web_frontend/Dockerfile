FROM node:12.15.0

WORKDIR /app
ADD . /app/

RUN npm i -g yarn --force

RUN yarn install
RUN yarn build

CMD [ "yarn", "start" ]
