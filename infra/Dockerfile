FROM python:3.11-slim
WORKDIR /app
COPY apps/api/requirements.txt ./
RUN pip install -r requirements.txt
COPY apps/api ./apps/api
CMD ["uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
