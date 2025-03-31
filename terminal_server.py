import os
import subprocess
from mcp.server.fastmcp import FastMCP

# Create an instance of FastMCP server with a name 'terminal'
mcp = FastMCP("terminal")

# Define the default workspace path using the home directory path expansion
DEFAULT_WORKSPACE = os.path.expanduser(r"~\mcp\workspace")


@mcp.tool()  # Decorator from the mcp framework (likely used for some MCP-related tools)
async def run_command(command: str):  # Function that accepts a terminal command as a string
    """  
    Run a terminal command inside the workspace directory. 

    Args:
         command: The shell command to run.

     Returns:
          The command output or error message. 
    """
    try:
        # Use subprocess to run the command in the specified directory
        result = subprocess.run(
            command,                  # The command to run (a string)
            shell=True,                # Use the shell to execute the command
            cwd=DEFAULT_WORKSPACE,     # Set the current working directory to DEFAULT_WORKSPACE
            capture_output=True,       # Capture standard output and error
            text=True                  # Return output as a string (instead of bytes)
        )
        
        # Return either the standard output or error if the output is empty
        return result.stdout or result.stderr
    
    except Exception as e:
        # If an error occurs, return the exception message as a string
        return str(e)

if __name__ == "__main__":
    mcp.run(transport='stdio')

