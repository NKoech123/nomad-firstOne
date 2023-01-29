A platform that allows customers to easily track and purchase food from their favorite food trucks. The platform uses GPS technology to display the location of food trucks in real time, making it easy for customers to find and support their favorite mobile vendors. Customers can browse menus, place orders, and pay for their meals directly through the platform, making the entire process seamless and convenient. With the ability to support local food truck businesses and discover new culinary experiences, the platform has quickly become a hit among foodies and food truck enthusiasts alike.

## Mobile
The backend utilizes the following tech-stack:
* [React Native](https://reactnative.dev/)
* [TyeScript](https://www.typescriptlang.org/)

At folder's root, run:
```
yarn install 
```
```
yarn start
```

## Backend
The backend utilizes the following tech-stack:

* 🐳 [Dockerized](https://www.docker.com/)
* [Express](https://expressjs.com/)
* [Prisma](https://www.prisma.io/)

### Run With Docker
You must have ```docker``` and ```docker-compose``` tools installed to work with material in this section.
Head to the ```/backend``` folder of the project.
Spin-up docker
```
docker-compose up -d
```
Run Migrations
```
yarn prisma migrate dev --name init
```
Run Server
```
yarn ts-node src/index.ts
```
REST API server ready at: http://localhost:3000


<img width="1073" alt="Screenshot 2023-01-24 at 9 11 10 PM" src="https://user-images.githubusercontent.com/84946242/214374409-5da5c764-e9f3-4622-8baf-a3ca8b643324.png">
