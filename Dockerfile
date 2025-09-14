FROM rasa/rasa-sdk:3.6.2
WORKDIR /app
COPY actions /app/actions
RUN pip install --no-cache-dir requests stripe tonweb
CMD ["start", "--actions", "actions"]
