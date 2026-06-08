import  json
from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

print("AI News Summarizer is starting...")
print("Paste your text and I will summarize it for you!")

while True:
    text = input("\nPaste your text (or type 'quit' to exit): ")
    
    if text.lower() == "quit":
        print("Goodbye! Come back to summarize more text!")
        break

    print("Got it! Summarizing...")

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a text summarizer. When given text, provide: 1) A 3 sentence summary 2) 5 key points 3) The main topic in one word."},
                {"role": "user", "content": "Please summarize this text: " + text}
            ]
        )
        summary = response.choices[0].message.content
        print("\nHere is your summary:")
        print(summary)
        session = {
            "original_text": text,
            "summary": summary
        }

        data = []
        try:
            with open("summaries.json", "r") as f:
                data = json.load(f)
        except:
            pass

        data.append(session)

        with open("summaries.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nSummary saved to summaries.json!")
    except Exception as e:
        print("Error:", e)
        continue