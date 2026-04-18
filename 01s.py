def agent_loop(state):
  response = client.messages.create(
    model = MODEL,
    system = SYSTEM,
    messages = state["messages"],
    
    
