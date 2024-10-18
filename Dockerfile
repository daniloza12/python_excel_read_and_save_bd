FROM python:3.12-slim

COPY . /app
WORKDIR /app

RUN mkdir -p /app/logs
RUN pip install -r requirements.txt

CMD ["python3","python_excel_process.py"]