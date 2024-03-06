FROM python:3.9-slim 

WORKDIR /code  

COPY requirements_server.txt ./  

RUN pip install -r requirements_server.txt 

COPY main.py .  

EXPOSE 8000  

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]