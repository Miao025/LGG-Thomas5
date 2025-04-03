FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /leaders
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD uvicorn app:app --host 0.0.0.0 --port $PORT
