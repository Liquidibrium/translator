docker build -t liquidibrium/translator:latest .
docker run -p 8080:5555 --name translator -e PORT=5555 liquidibrium/translator:latest