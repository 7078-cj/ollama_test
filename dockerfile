FROM ollama/ollama:latest

ENV OLLAMA_HOST=0.0.0.0
EXPOSE 11434

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]