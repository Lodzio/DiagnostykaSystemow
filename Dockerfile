FROM tensorflow/tensorflow:latest-gpu
WORKDIR /workspace
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "index.py"]