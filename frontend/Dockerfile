# Use the official Node.js image as the base image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the application code to the working directory
COPY . .

# Build the Next.js app
RUN yarn build

# Expose port 3000 to the outside world
EXPOSE 3000

# Start the Next.js app
CMD ["yarn", "start"]
