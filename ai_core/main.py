from utils.email_reader import email_reader
from nlp.preprocess_email import preprocess_email_spacy
from agents.category_classifier import get_category
from agents.response_genarator import get_response
import asyncio

if __name__ == "__main__":
    async def main():
        email_example = (
            "Prezado Suporte,\n\n"
            "Gostaria de Atualizações sobre casos em aberto."
            "\n\n"
            "Atenciosamente,\nEmanuel Duarte"
        )
        
        # Step 1: Read the email content
        preprocess_email_spacy(email_example)

        # Step 2: Classify the email category
        category = await get_category(email_example)
        print(f"Classified Category: {category}")

        # Step 3: Generate a response based on the email content and category
        response = await get_response(email_example, category)
        print(f"Generated Response:\n{response}")
        print("Email processing completed.")

    asyncio.run(main())
