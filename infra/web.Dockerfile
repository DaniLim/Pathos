FROM python:3.11-slim
WORKDIR /web
COPY apps/web ./
CMD ["python", "-m", "http.server", "3000"]
