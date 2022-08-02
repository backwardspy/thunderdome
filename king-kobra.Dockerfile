FROM node AS build

WORKDIR /app

COPY package*.json .
RUN npm ci

COPY . .
RUN npm run build

RUN ls -lah build

FROM node

WORKDIR /app

COPY package*.json .
RUN npm ci --production

COPY --from=build /app/build/* .

RUN ls -lah

CMD ["node", "index.js"]

