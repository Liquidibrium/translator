docker build -t translator:latest .
docker run -p 8080:8080 --rm --name translator translator:latest