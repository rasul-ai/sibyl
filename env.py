from azureml.core import Workspace, Environment

ws = Workspace.from_config()  # Assumes config.json is present in the current directory
# Replace 'myenv' with a unique name for your environment
env = Environment.from_pip_requirements(name="agentic-env-sibyl", file_path="/home/bapary/Work/RiashatVai/agentic-llm/Sibyl-System/requirements.txt")

# This step allows you to reuse the environment later
env.register(workspace=ws)
print(f"Environment registered as: {env.name}")

