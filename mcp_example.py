"""
Example: Using MCP Context with Claude Wrapper
Run this script to see MCP context in action
"""

from claude_wrapper import ClaudeWrapper, MCPContextProvider

# Initialize
api_key = open('.env').read().strip()
wrapper = ClaudeWrapper(api_key=api_key)
mcp = MCPContextProvider()

print("=" * 70)
print("MCP CONTEXT EXAMPLE")
print("=" * 70)

# EXAMPLE 1: Professional Context
print("\n🎯 EXAMPLE 1: Professional Context")
print("-" * 70)

mcp.add_context("role", "Senior consultant at BCG")
mcp.add_context("expertise", "Infrastructure, waste management, energy")
mcp.add_context("location", "Working on projects in Southeast Asia")

print("Added contexts:", mcp.list_contexts())

response = wrapper.chat_with_context(
    "I need to present a waste-to-energy project proposal. What key points should I cover?",
    mcp.get_all_contexts()
)

print("\nQuestion: I need to present a waste-to-energy project proposal.")
print(f"Answer:\n{response}\n")

# EXAMPLE 2: Technical Context
print("\n💻 EXAMPLE 2: Technical Context")
print("-" * 70)

wrapper.clear_history()  # Start fresh conversation
mcp2 = MCPContextProvider()

mcp2.add_context("tech_stack", "Python 3.9, Flask, PostgreSQL, Docker")
mcp2.add_context("team_size", "5 developers, 2 month timeline")
mcp2.add_context("requirements", "API must handle 50K req/day, <200ms response time")

print("Added contexts:", mcp2.list_contexts())

response = wrapper.chat_with_context(
    "Design the database schema for tracking industrial waste disposal",
    mcp2.get_all_contexts()
)

print("\nQuestion: Design the database schema for tracking industrial waste disposal")
print(f"Answer:\n{response}\n")

# EXAMPLE 3: Meeting Notes Context
print("\n📝 EXAMPLE 3: Using Meeting Notes as Context")
print("-" * 70)

wrapper.clear_history()
mcp3 = MCPContextProvider()

mcp3.add_context("meeting_notes", """
Client Meeting - Dec 19, 2025:
- Client: Jakarta Municipal Waste Authority
- Budget: $2M for Phase 1
- Timeline: 6 months MVP, full deployment in 18 months
- Key features needed:
  * Real-time waste tracking dashboard
  * Mobile app for collection drivers
  * Compliance reporting (Indonesian regulations)
  * Integration with existing city database
- Technical constraints:
  * Must work offline in remote areas
  * Support for 1000+ concurrent users
  * Multi-language (Indonesian, English)
""")

response = wrapper.chat_with_context(
    "Based on the meeting notes, create a prioritized feature roadmap",
    mcp3.get_all_contexts()
)

print("Question: Based on the meeting notes, create a prioritized feature roadmap")
print(f"Answer:\n{response}\n")

print("=" * 70)
print("💡 TIP: Update contexts as your project evolves!")
print("=" * 70)
