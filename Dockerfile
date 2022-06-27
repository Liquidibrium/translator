FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common

RUN apt-get install -y build-essential cmake unzip pkg-config
RUN apt-get install -y python3-pip python3-dev libgl1-mesa-glx 
RUN apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
RUN apt-get install -y libxvidcore-dev libx264-dev
RUN apt-get install -y libgtk-3-dev
RUN apt-get install -y libatlas-base-dev gfortran

#RUN apt-get install -y ttf-mscorefonts-installer
RUN apt-get install -y tesseract-ocr-deu

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
#RUN add-apt-repository ppa:alex-p/tesseract-ocr5
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -q -r requirements.txt

COPY . /app/

CMD ["python", "server.py"]