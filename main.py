from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Smithery Test")

@mcp.tool()
def custom_greet(name: str) -> str:
    """
    Returns a Custom Greet.
    
    Args:
        name (str): Name
    
    Returns:
        str: Greet Response
    """
    
    return f"Hey {name}"

if __name__ == "__main__":
    # This will run the MCP server when the script is executed.
    mcp.run()