import os

# Base directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path for the prompts directory
PROMPTS_DIR = os.path.join(BASE_DIR, "..", "prompts")

"""Module to load system prompts from files."""
def prompt_loader(agent_name: str) -> str:
    # Base path to the prompt file
    prompt_path = os.path.abspath(os.path.join(PROMPTS_DIR, agent_name))

    try:
        with open(prompt_path, "r", encoding="utf-8") as file:
            system_prompt = file.read()
        return system_prompt

    except FileNotFoundError:
        raise FileNotFoundError(f"System prompt file not found at {prompt_path}")
    except Exception as e:
        raise Exception(f"An error occurred while loading the system prompt: {e}")
