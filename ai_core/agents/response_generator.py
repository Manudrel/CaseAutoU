from ai_core.utils.prompt_loader import prompt_loader
from groq import Groq, APIConnectionError, APIStatusError
from dotenv import load_dotenv
import os

load_dotenv()
# Get Groq API key from environment variable
api_key = os.getenv('GROQ_API_KEY_RESPONSE')

if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set.")

# Initialize Groq client
client = Groq(api_key=api_key)


async def get_response(email_text: str, category: str) -> str:
    
    """Get category from Groq API based on the email message and the."""
    try:
        
        system_prompt = prompt_loader("response_genarator.txt")
        
        # Prepare the messages for the chat completion
        messages: list= [
            {
                "role": "system", 
                "content": f"{system_prompt}"
            }
        ]
        
        messages.extend([
            {"role": "user", "content": f"**{category}**"}])
        
        # Adds the actual email prompt at the end
        messages.append({"role": "user", "content": email_text})
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages= messages, 
            temperature=0.5,
            max_completion_tokens = 1000,
            top_p=0.5,
        )
        return completion.choices[0].message.content or ""
    
    
    except APIConnectionError as e:
        return f"Connection Error: {e}"
    except APIStatusError as e:
        return f"API Error: {e.status_code}"
    except Exception as e:
        return f"Unexpected Error: {e}"
