import os
from markitdown import MarkItDown
from mcp.server.fastmcp import FastMCP

# Создаем MCP сервер
mcp = FastMCP("MarkItDown Service", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
md = MarkItDown()

@mcp.tool()
def convert_to_markdown(file_url: str) -> str:
    """Конвертирует документ по URL в формат Markdown."""
    try:
        result = md.convert(file_url)
        return result.text_content
    except Exception as e:
        return f"Ошибка при конвертации: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="sse")