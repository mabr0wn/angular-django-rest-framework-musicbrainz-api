# base image
FROM node:latest

# set working directory
WORKDIR /usr/src/app/

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app
RUN yarn install

COPY . /usr/src/app/

EXPOSE 4000

# start app
CMD ["yarn", "start"]