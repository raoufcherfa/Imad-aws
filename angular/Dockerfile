# Use Node.js as the base image for the build stage
FROM node:14 AS build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./
# Copy the remaining files to the container
COPY . .

# Install the required packages
RUN npm install

# Build the Angular application
RUN npm run build --prod

# Use NGINX as the base image for the production stage
FROM nginx:1.19

EXPOSE 4200

# Copy the built Angular application from the build stage
COPY --from=build /app/dist/angular-frontend /usr/share/nginx/html

