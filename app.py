"""
Flask Web Interface for Claude Wrapper
Simple web UI to interact with the wrapper
"""

from flask import Flask, render_template, request, jsonify, session
from claude_wrapper import ClaudeWrapper, MCPContextProvider
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Store wrappers per session (in production, use proper session management)
wrappers = {}
mcp_providers = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    user_message = data.get('message', '')
    use_context = data.get('use_context', False)
    api_key = data.get('api_key', '')
    
    if not api_key:
        return jsonify({'error': 'API key required'}), 400
    
    # Get or create wrapper for this session
    session_id = session.get('session_id', secrets.token_hex(8))
    session['session_id'] = session_id
    
    if session_id not in wrappers:
        wrappers[session_id] = ClaudeWrapper(api_key)
        mcp_providers[session_id] = MCPContextProvider()
    
    wrapper = wrappers[session_id]
    mcp = mcp_providers[session_id]
    
    try:
        if use_context and mcp.list_contexts():
            response = wrapper.chat_with_context(user_message, mcp.get_all_contexts())
        else:
            response = wrapper.chat(user_message)
        
        return jsonify({
            'response': response,
            'history_length': len(wrapper.get_history())
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/context', methods=['POST'])
def add_context():
    """Add context to MCP provider"""
    data = request.json
    name = data.get('name', '')
    content = data.get('content', '')
    
    session_id = session.get('session_id')
    if not session_id or session_id not in mcp_providers:
        return jsonify({'error': 'No active session'}), 400
    
    mcp = mcp_providers[session_id]
    mcp.add_context(name, content)
    
    return jsonify({
        'success': True,
        'contexts': mcp.list_contexts()
    })

@app.route('/api/contexts', methods=['GET'])
def list_contexts():
    """List all contexts"""
    session_id = session.get('session_id')
    if not session_id or session_id not in mcp_providers:
        return jsonify({'contexts': []})
    
    mcp = mcp_providers[session_id]
    return jsonify({
        'contexts': mcp.list_contexts()
    })

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    session_id = session.get('session_id')
    if not session_id or session_id not in wrappers:
        return jsonify({'history': []})
    
    wrapper = wrappers[session_id]
    return jsonify({
        'history': wrapper.get_history()
    })

@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear conversation history"""
    session_id = session.get('session_id')
    if not session_id or session_id not in wrappers:
        return jsonify({'error': 'No active session'}), 400
    
    wrapper = wrappers[session_id]
    wrapper.clear_history()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
