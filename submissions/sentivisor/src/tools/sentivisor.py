from agno.tools import tool
import os
from agno.tools.zoom import ZoomTools

@tool
def this_is_a_tool(tool_input: str) -> str:
    """
    Tool description
    """
    return "Tool response"

def this_is_not_a_tool(tool_input: str) -> str:
    """
    This is not a tool
    """
    return "This is not a tool"

# Get environment variables
ACCOUNT_ID = os.getenv("ZOOM_ACCOUNT_ID")
CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")

# Initialize Zoom tools with credentials
zoom_tools = ZoomTools(
    account_id=ACCOUNT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)