#!/bin/sh
# Start Ollama in background
ollama serve &

# Wait a few seconds for server to be ready
sleep 5

# Pull the model if not already present
if ! ollama list | grep -q "qwen2.5:0.5b"; then
    ollama pull qwen2.5:0.5b
fi

# Keep the server running in the foreground
wait