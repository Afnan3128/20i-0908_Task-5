# frontend/Dockerfile
FROM nginx:alpine

# Copy the frontend files into the nginx server
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Command to run nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
