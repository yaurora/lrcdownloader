FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py", "/music", "https://lrc.xms.mx/lyrics", "/lyrics"]
