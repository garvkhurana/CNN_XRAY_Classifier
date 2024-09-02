FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements2.txt
EXPOSE 3000
CMD ["python", "app.py"]