from fastmcp import FastMCP
import requests

mcp = FastMCP("Weather MCP Server")   # creates a new FastMCP server instance

@mcp.tool()   # decorator to register this function as an MCP tool under server instance mcp
def get_weather(city: str) -> str:  

    api_key = "2c659ee2cb08342d8639dc6d581c68ca"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"According to the weather API, it's {weather}, {temp}°C."
        else:
            return f"Error getting weather for {city}: {data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)