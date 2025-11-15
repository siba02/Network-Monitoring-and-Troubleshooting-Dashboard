FROM python:3.10-slim

RUN pip install psutil

WORKDIR /app
COPY agent.py /app/agent.py

CMD ["python3", "agent.py"]
