chepy_mcp is an implementation of a Model Context Protocol (MCP) server using Chepy. The implementation sets up the Chepy instance to 
be used to parse a command and return the result of the processed command to the user.

Some todo features are:
   1. Add more extensively to the methods.
   2. Test and intall on different operating systems.
   3. Accept and deploy any useful pull requests. 

## Usage

To use the mcp protocol, open claude desktop app and open the AI settings tab. Ensure that Local AI Servers is on and click Configure. Set a random port that is not occupied and for the localserver url, enter
```bash
python -m chepy_mcp.tcp
```

This starts a tcp server on port 12345 (default) waiting for input from claude desktop app.
