# Quick Start Guide

## What You've Got

A complete Claude API wrapper with:
- Python backend (Flask)
- Web interface
- MCP-like context injection
- Conversation management

## Files

```
claude-wrapper/
├── claude_wrapper.py       # Core wrapper classes
├── app.py                  # Flask web server
├── templates/
│   └── index.html         # Web UI
├── requirements.txt       # Dependencies
├── README.md             # Full documentation
├── demo_standalone.py    # Demo without API needed
└── QUICK_START.md        # This file
```

## Setup (5 minutes)

### 1. Install Dependencies

```bash
pip install anthropic flask
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### 2. Get Your API Key

Go to: https://console.anthropic.com
- Sign up or log in
- Get your API key

### 3. Run the Web App

```bash
python app.py
```

### 4. Open Browser

Navigate to: http://localhost:5000

### 5. Start Chatting!

- Enter your API key in the sidebar
- Type a message
- Watch it work!

## Quick Test (No Web UI)

```python
from claude_wrapper import ClaudeWrapper

# Initialize
wrapper = ClaudeWrapper(api_key="your-api-key-here")

# Send a message
response = wrapper.chat("Hello! Tell me a fun fact.")
print(response)

# Check history
print(f"Messages in history: {len(wrapper.get_history())}")

# Save conversation
wrapper.save_conversation("my_chat.json")
```

## Try the MCP Context Feature

```python
from claude_wrapper import ClaudeWrapper, MCPContextProvider

wrapper = ClaudeWrapper(api_key="your-key")
mcp = MCPContextProvider()

# Add context about yourself
mcp.add_context("background", "I'm a consultant at BCG")
mcp.add_context("interest", "Learning about AI and APIs")

# Chat with this context
response = wrapper.chat_with_context(
    "Give me advice on learning Python",
    mcp.get_all_contexts()
)
```

Claude will now tailor responses based on your background!

## View Demo (No API Key Needed)

```bash
python demo_standalone.py
```

This shows you how everything works without needing an API key.

## What's Next?

1. Read `README.md` for full documentation
2. Modify `claude_wrapper.py` to add your own features
3. Customize `templates/index.html` for your UI preferences
4. Add new endpoints in `app.py`

## Common Issues

**"No module named 'anthropic'"**
→ Run: `pip install anthropic`

**"API key required"**
→ Get key from console.anthropic.com

**"Port 5000 in use"**
→ Change port in `app.py`: `app.run(port=5001)`

## Features to Explore

✅ Automatic history management
✅ Context injection
✅ Save/load conversations
✅ Conversation summaries
✅ Timestamped messages
✅ Web interface

## Need Help?

Check out:
- README.md - Full documentation
- demo_standalone.py - See it in action
- Anthropic docs - https://docs.anthropic.com

---

Happy coding! 🚀
