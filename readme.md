# Claude Wrapper - Practice Project

A simple Claude API wrapper with MCP-like context injection for learning purposes.

## Features

✅ **Core Wrapper Features:**
- Automatic conversation history management
- Timestamped messages
- Save/load conversations
- Conversation summaries
- Context injection (MCP-like)

✅ **Web Interface:**
- Clean, modern UI
- Real-time chat
- MCP context management
- History tracking

## What Makes This a "Wrapper"?

This project wraps Claude's API by adding:
1. **State Management** - Maintains conversation history automatically
2. **Context Injection** - Simulates MCP by injecting context into system prompts
3. **Enhanced Features** - Save/load, summaries, timestamps
4. **Custom Interface** - Web UI instead of just API calls

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Anthropic API key from: https://console.anthropic.com

3. Run the Flask app:
```bash
python app.py
```

4. Open browser to: http://localhost:5000

## Usage

### Web Interface

1. Enter your API key in the sidebar
2. (Optional) Add MCP contexts:
   - Name: `user_profile`
   - Content: `User is a developer interested in AI`
3. Type messages and chat with Claude
4. Toggle "Use MCP Context" to include contexts in requests

### Programmatic Usage

```python
from claude_wrapper import ClaudeWrapper, MCPContextProvider

# Initialize
wrapper = ClaudeWrapper(api_key="your-api-key")
mcp = MCPContextProvider()

# Add context
mcp.add_context("user_info", "User is learning Python")
mcp.add_context("project", "Building a REST API")

# Chat with context
response = wrapper.chat_with_context(
    "Help me design an API endpoint",
    mcp.get_all_contexts()
)

# Or chat without context
response = wrapper.chat("What's the weather like?")

# Save conversation
wrapper.save_conversation("my_chat.json")

# Get summary
summary = wrapper.get_summary()
```

## Architecture

```
┌─────────────────┐
│   Web UI        │
│  (index.html)   │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   Flask App     │
│   (app.py)      │
└────────┬────────┘
         │
         ↓
┌─────────────────┐      ┌──────────────────┐
│ ClaudeWrapper   │◄─────┤ MCPContextProvider│
│ (claude_wrapper)│      │ (context injection)│
└────────┬────────┘      └──────────────────┘
         │
         ↓
┌─────────────────┐
│  Anthropic API  │
│  (Claude)       │
└─────────────────┘
```

## What is MCP?

Model Context Protocol (MCP) is a way to provide external context to AI models. This wrapper simulates MCP by:

1. Storing named contexts (user profile, project info, etc.)
2. Injecting them into the system prompt
3. Allowing Claude to use this context when responding

## Learning Points

This project demonstrates:

- **API Integration**: Working with Anthropic's Python SDK
- **State Management**: Maintaining conversation context
- **Web Development**: Flask backend + vanilla JS frontend
- **Context Injection**: Simulating MCP-like functionality
- **Clean Code**: Modular, documented Python code

## Next Steps to Enhance

1. **Add authentication** - Secure API key storage
2. **Database integration** - Persist conversations
3. **Real MCP integration** - Connect to actual MCP servers
4. **Streaming responses** - Live token streaming
5. **Multiple conversations** - Manage multiple chat sessions
6. **Export features** - Export to PDF, Markdown
7. **Advanced contexts** - File uploads, web scraping
8. **Rate limiting** - Prevent API abuse
9. **Cost tracking** - Monitor token usage

## Why This is Useful

Even though this is a "wrapper," it adds value by:
- Simplifying common patterns (history, context)
- Providing a custom UI for specific use cases
- Making API integration easier for beginners
- Demonstrating how to build on top of AI APIs

## License

MIT - Free to use for learning and practice
