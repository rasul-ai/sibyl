pip install --upgrade opencv-python==4.5.5.64 opencv-python-headless==4.5.5.64
pip ps aux | grep ollamainstall langchain-ollama
pip install langchain langchain-community datasets -U

huggingface-cli login --token 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
apt-get update
apt-get install lshw
pip install 'litellm[proxy]'
curl -fsSL https://ollama.com/install.sh | sh
ps aux | grep ollama
litellm --model ollama/llama3:instruct

In Another Terminal:
ollama pull llama3:instruct
python main_m.py



AZURE_URL="https://allam-swn-gpt-01.openai.azure.com/openai/deployments/gpt-4o-900ptu/chat/completions?api-version=2024-02-15-preview"
GPT_ENGINE="gpt-4o-900ptu"
AZURE_API_KEY="8af2cca79fb34601ab829b44b7fa6dcf"