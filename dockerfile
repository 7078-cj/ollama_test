# Use official Ollama image
FROM ollama/ollama:latest

# Bind to all interfaces
ENV OLLAMA_HOST=0.0.0.0

# Expose Ollama default port
EXPOSE 11434

# Pull the model at build time
RUN ollama pull qwen2.5:0.5b

# Start Ollama when the container runs
CMD ["ollama", "serve"]