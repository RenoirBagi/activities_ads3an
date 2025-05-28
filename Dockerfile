FROM python:3.12

WORKDIR /atividade-app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 5002

CMD ["python", "atividade_service/app.py"]