# Use official Ollama image
FROM ollama/ollama:latest

# Expose Ollama default port
EXPOSE 11434


RUN ollama serve & \
    sleep 5 && \
    ollama pull qwen2.5:0.5b

# Start Ollama when container runs
CMD ["ollama", "serve"]