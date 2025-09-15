from fastmcp import Client
import google.generativeai as genai
import os
import asyncio

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_city(question: str) -> str:
    for city in ("Hyderabad","Bangalore","Mumbai","Delhi","Chennai"):
        if city.lower() in question.lower():
            return city
    return "Hyderabad"

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        question = input("Out of Hyderabad, Bangalore, Mumbai, Delhi, Chennai, which city's weather details do you want").strip()
        result = await client.call_tool("get_weather", {"city": extract_city(question)})
        weather_text = result.content

        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = (
            f"User asked: {question}\n"
            f"Weather data: {weather_text}\n"
            "Please answer naturally."
        )
        response = model.generate_content(prompt)
        print(response.text)

if __name__ == "__main__":
    asyncio.run(main())

    