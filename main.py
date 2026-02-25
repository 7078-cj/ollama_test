import requests
import json

BASE_URL = "http://localhost:11434"

def check_server():
    try:
        response = requests.get(f"{BASE_URL}/api/tags", timeout=10)
        if response.status_code == 200:
            print("✅ Ollama server is running.")
            print("Available models:")
            print(json.dumps(response.json(), indent=2))
        else:
            print("❌ Server responded but with status:", response.status_code)
    except Exception as e:
        print("❌ Cannot connect to Ollama:", e)


def test_generation():
    payload = {
        "model": "gemma3:4b",
        "prompt": "Explain artificial intelligence in simple words.",
        "stream": False
    }

    try:
        response = requests.post(
            f"{BASE_URL}/api/generate",
            json=payload,
            timeout=120
        )

        if response.status_code == 200:
            data = response.json()
            print("\n🧠 Model Response:\n")
            print(data["response"])
        else:
            print("❌ Generation failed:", response.status_code, response.text)

    except Exception as e:
        print("❌ Error during generation:", e)


if __name__ == "__main__":
    print("🔎 Checking Ollama server...\n")
    check_server()

    print("\n🚀 Testing generation...\n")
    test_generation()