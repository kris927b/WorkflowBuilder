# Use the official Node.js image.
# https://hub.docker.com/_/node
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY package.json .

# Install dependencies
RUN npm install

# Copy the content of the frontend directory to the working directory
COPY . .

# Start the React app
CMD ["npm", "start"]
