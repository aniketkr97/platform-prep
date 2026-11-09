# Broken on purpose: docker stop takes the full timeout and in-flight requests die.
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py entrypoint.sh /app/
EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
