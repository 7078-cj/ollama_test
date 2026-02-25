# Use official Ollama image
FROM ollama/ollama:latest

# Expose Ollama default port
EXPOSE 11434

# Start Ollama service and pull gemma3:4b
RUN ollama serve & \
    sleep 5 && \
    ollama pull gemma3:4b

# Start Ollama when container runs
CMD ["ollama", "serve"]