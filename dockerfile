FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
EXPOSE 8501
EXPOSE 8080

CMD [ "sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 --log-level debug & streamlit run UI.py --server.port 8501 --server.address 0.0.0.0 && wait"]