"""
Simple Claude API Wrapper with MCP Integration
A practice project demonstrating how to wrap Claude's API with additional features
"""

import anthropic
import json
from datetime import datetime
from typing import List, Dict, Optional

class ClaudeWrapper:
    def __init__(self, api_key: str):
        """Initialize the Claude wrapper with API key"""
        self.client = anthropic.Anthropic(api_key=api_key)
        self.conversation_history = []
        self.model = "claude-sonnet-4-20250514"
        
    def chat(self, user_message: str, system_prompt: Optional[str] = None) -> str:
        """
        Send a message to Claude and get a response
        Maintains conversation history automatically
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat()
        })

        # Prepare messages for API (without timestamps)
        api_messages = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in self.conversation_history
            if msg["role"] in ["user", "assistant"]
        ]

        # Inject current date/time into system prompt
        current_time = datetime.now()
        date_context = f"Current date and time: {current_time.strftime('%A, %B %d, %Y at %I:%M %p')}"

        if system_prompt:
            enhanced_system_prompt = f"{date_context}\n\n{system_prompt}"
        else:
            enhanced_system_prompt = f"{date_context}\n\nYou are a helpful AI assistant."

        # Make API call
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            system=enhanced_system_prompt,
            messages=api_messages
        )
        
        # Extract response text
        assistant_message = response.content[0].text
        
        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message,
            "timestamp": datetime.now().isoformat()
        })
        
        return assistant_message
    
    def chat_with_context(self, user_message: str, context: str) -> str:
        """
        Chat with additional context injected into the system prompt
        Useful for MCP-like context injection
        """
        system_prompt = f"""You are a helpful AI assistant.

Additional Context:
{context}

Use this context to inform your responses when relevant."""
        
        return self.chat(user_message, system_prompt)
    
    def get_history(self) -> List[Dict]:
        """Return the full conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        
    def save_conversation(self, filename: str):
        """Save conversation to JSON file"""
        with open(filename, 'w') as f:
            json.dump({
                "model": self.model,
                "conversation": self.conversation_history
            }, f, indent=2)
        print(f"Conversation saved to {filename}")
    
    def load_conversation(self, filename: str):
        """Load conversation from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.conversation_history = data["conversation"]
        print(f"Conversation loaded from {filename}")
    
    def get_summary(self) -> str:
        """Get a summary of the current conversation"""
        if not self.conversation_history:
            return "No conversation history yet."
        
        summary_prompt = """Please provide a brief summary of our conversation so far. 
        Keep it to 2-3 sentences."""
        
        return self.chat(summary_prompt)


class MCPContextProvider:
    """
    Simple MCP-like context provider
    Simulates providing external context to Claude
    """
    def __init__(self):
        self.contexts = {}
    
    def add_context(self, name: str, content: str):
        """Add a named context"""
        self.contexts[name] = {
            "content": content,
            "added_at": datetime.now().isoformat()
        }
    
    def get_context(self, name: str) -> Optional[str]:
        """Get a specific context"""
        return self.contexts.get(name, {}).get("content")
    
    def get_all_contexts(self) -> str:
        """Get all contexts formatted for injection"""
        if not self.contexts:
            return ""
        
        formatted = []
        for name, data in self.contexts.items():
            formatted.append(f"[{name}]\n{data['content']}\n")
        
        return "\n".join(formatted)
    
    def list_contexts(self) -> List[str]:
        """List all context names"""
        return list(self.contexts.keys())


# Example usage
if __name__ == "__main__":
    print("Claude Wrapper Example")
    print("=" * 50)
    print("\nThis is a demo. In real usage, you'd provide your API key.")
    print("\nFeatures of this wrapper:")
    print("- Automatic conversation history management")
    print("- Context injection (MCP-like)")
    print("- Save/load conversations")
    print("- Conversation summaries")
    print("- Timestamped messages")
    
    # Example of how you'd use it:
    print("\n" + "=" * 50)
    print("Example Usage Code:")
    print("=" * 50)
    print("""
# Initialize wrapper
wrapper = ClaudeWrapper(api_key="your-api-key")

# Add MCP context
mcp = MCPContextProvider()
mcp.add_context("user_profile", "User is a developer learning AI")
mcp.add_context("project_info", "Working on a REST API with PostgreSQL")

# Chat with context
response = wrapper.chat_with_context(
    "Help me with API design",
    mcp.get_all_contexts()
)

# Save conversation
wrapper.save_conversation("my_chat.json")

# Get summary
summary = wrapper.get_summary()
    """)

