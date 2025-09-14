FROM rasa/rasa:3.6.19-full

WORKDIR /app

USER root

# Install additional dependencies
RUN pip install --no-cache-dir redis

USER 1001

# Copy the Rasa files
COPY --chown=1001:1001 . /app

# Set the user to run the application
USER 1001

# Train the model on build (optional)
# RUN rasa train

EXPOSE 5005