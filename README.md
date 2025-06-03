To run Sibyl follow these commands,
```
pip install --upgrade opencv-python==4.5.5.64 opencv-python-headless==4.5.5.64
pip ps aux | grep ollamainstall langchain-ollama
pip install langchain langchain-community datasets -U

huggingface-cli login --token <your token>
apt-get update
apt-get install lshw
pip install 'litellm[proxy]'
curl -fsSL https://ollama.com/install.sh | sh
ps aux | grep ollama
# litellm --model ollama/llama3:instruct
```

In another terminal,
```
ollama pull llama3:instruct
python main_m.py
```
