# Use official Ollama image
FROM ollama/ollama:latest

# Bind to all interfaces for Render
ENV OLLAMA_HOST=0.0.0.0

# Expose port (Render uses 11434 internally)
EXPOSE 11434

# Start server and pull lightweight model
CMD ollama serve & sleep 5 && ollama pull qwen2.5:0.5b && wait