FROM python:3.10-slim
RUN pip install flask
COPY app.py /app/app.py
COPY index.html /app/index.html
WORKDIR /app
CMD ["python3", "app.py"]
