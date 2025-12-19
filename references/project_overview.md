# Claude Wrapper - Project Overview

## 🎯 What This Is

A hands-on practice project that creates a "wrapper" around Claude's API. It demonstrates how to build on top of AI APIs while adding real value through state management, context injection, and a custom interface.

## 📦 Complete File Structure

```
claude-wrapper/
├── claude_wrapper.py       # Core wrapper implementation
│   ├── ClaudeWrapper       # Main wrapper class
│   └── MCPContextProvider  # Context management
│
├── app.py                  # Flask web application
│   ├── /api/chat          # Send messages
│   ├── /api/context       # Manage contexts
│   ├── /api/history       # View history
│   └── /api/clear         # Clear history
│
├── templates/
│   └── index.html         # Beautiful web UI
│
├── requirements.txt       # Python dependencies
├── README.md             # Full documentation
├── QUICK_START.md        # 5-minute setup guide
├── demo_standalone.py    # Demo without API
└── PROJECT_OVERVIEW.md   # This file
```

## 🚀 Key Concepts

### What's a "Wrapper"?

A wrapper is code that:
1. Uses an existing API (Claude in this case)
2. Adds a layer of functionality on top
3. Provides its own interface

Think of it like a smartphone case - it wraps the phone and adds features like a kickstand or card holder.

### What This Wrapper Adds

```
Raw Claude API          Your Wrapper
     ↓                       ↓
Send message       →  • Maintains history
Get response           • Injects context
                       • Timestamps messages
                       • Saves conversations
                       • Provides web UI
                       • Manages state
```

### MCP Context Injection

Model Context Protocol (MCP) provides external context to AI models. This wrapper simulates it:

```python
# Traditional way
response = claude.chat("Help me with Python")

# With context injection
mcp.add_context("background", "User is a senior consultant")
mcp.add_context("expertise", "Strategy, M&A, engineering")
response = wrapper.chat_with_context(
    "Help me with Python",
    mcp.get_all_contexts()
)
# Now Claude knows your background!
```

## 💡 Architecture

```
┌─────────────────────────────────────────────┐
│           Web Browser (User)                │
│         http://localhost:5000               │
└────────────────┬────────────────────────────┘
                 │
                 ↓ HTTP POST
┌─────────────────────────────────────────────┐
│         Flask App (app.py)                  │
│  • Routes                                   │
│  • Session management                       │
│  • Request handling                         │
└────────────────┬────────────────────────────┘
                 │
                 ↓ Python calls
┌─────────────────────────────────────────────┐
│    ClaudeWrapper (claude_wrapper.py)        │
│  • Conversation history                     │
│  • State management                         │
│  • Context injection                        │
│  • Save/load features                       │
└────────────────┬────────────────────────────┘
                 │
                 ↓ API calls
┌─────────────────────────────────────────────┐
│         Anthropic API (Claude)              │
│  • AI model processing                      │
│  • Response generation                      │
└─────────────────────────────────────────────┘
```

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **AI SDK**: Anthropic Python SDK
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **State**: In-memory (session-based)
- **API**: RESTful endpoints

## 📚 What You'll Learn

### 1. API Integration
- Using the Anthropic Python SDK
- Managing API keys securely
- Handling API responses and errors

### 2. State Management
- Maintaining conversation history
- Session handling in Flask
- Managing context across requests

### 3. Web Development
- Flask routing and endpoints
- RESTful API design
- Single-page application patterns
- Async JavaScript (fetch API)

### 4. Software Architecture
- Modular code design
- Separation of concerns
- Clean API interfaces

### 5. Context Injection
- System prompt engineering
- Context formatting
- Dynamic prompt construction

## 🎓 Learning Path

### Beginner (30 minutes)
1. Run `python demo_standalone.py` to see how it works
2. Read through `claude_wrapper.py` 
3. Try running the web app locally

### Intermediate (2 hours)
1. Add your own context types
2. Customize the web UI
3. Add new API endpoints
4. Implement conversation export to Markdown

### Advanced (1 day)
1. Add streaming responses
2. Implement database persistence
3. Add user authentication
4. Create conversation branching
5. Add file upload for contexts
6. Implement token cost tracking

## 🔧 Extension Ideas

### Easy Additions
- [ ] Export to Markdown
- [ ] Dark mode toggle
- [ ] Keyboard shortcuts
- [ ] Message search
- [ ] Copy message button

### Medium Complexity
- [ ] Multiple conversation threads
- [ ] Conversation sharing
- [ ] Template prompts
- [ ] Context from files
- [ ] Response regeneration

### Advanced Features
- [ ] Real-time streaming
- [ ] Database persistence (PostgreSQL)
- [ ] User authentication
- [ ] Team workspaces
- [ ] API rate limiting
- [ ] Cost analytics
- [ ] Prompt templates
- [ ] Webhook integrations

## 📊 Comparison to Raw API

| Feature | Raw Claude API | This Wrapper |
|---------|---------------|--------------|
| Send message | ✅ | ✅ |
| Get response | ✅ | ✅ |
| History management | ❌ Manual | ✅ Automatic |
| Context injection | ❌ Manual | ✅ Built-in |
| Web interface | ❌ | ✅ |
| Save conversations | ❌ | ✅ |
| Timestamps | ❌ | ✅ |
| Summaries | ❌ | ✅ |

## 🎯 Use Cases

This wrapper pattern is useful for:

1. **Learning Projects**: Understand API integration
2. **Rapid Prototyping**: Test ideas quickly
3. **Custom Workflows**: Add domain-specific features
4. **Internal Tools**: Build company-specific assistants
5. **Portfolio Projects**: Demonstrate full-stack skills

## 🚦 Getting Started

### Quickest Path (3 minutes)
```bash
python demo_standalone.py
```

### Full Setup (5 minutes)
```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

### Try Programmatically
```python
from claude_wrapper import ClaudeWrapper

wrapper = ClaudeWrapper(api_key="your-key")
response = wrapper.chat("Hello!")
print(response)
```

## 📖 Documentation

- **QUICK_START.md**: 5-minute setup guide
- **README.md**: Complete documentation
- **demo_standalone.py**: Interactive demo
- **Code comments**: Inline documentation

## 🤝 Next Steps

1. **Run the demo** to see it in action
2. **Read the code** to understand the patterns
3. **Modify it** to add your own features
4. **Build something** using these patterns

## 💪 Skills You'll Practice

- Python programming
- API integration
- Web development
- State management
- System design
- Documentation
- Code organization

## 🎉 Have Fun!

This is a learning project, so:
- Experiment freely
- Break things and fix them
- Add wild features
- Share what you build

---

**Built for learning and practice**  
Feel free to modify, extend, and make it your own!
