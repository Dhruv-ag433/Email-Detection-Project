FROM python:3.12.0

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
EXPOSE 8501

CMD [ "sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run UI.py --server.port 8501 --server.address 0.0.0.0"]