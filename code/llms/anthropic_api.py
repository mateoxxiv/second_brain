"""
Anthropic Claude API — Practical Examples
==========================================
Demonstrates: basic calls, system prompts, multi-turn conversations,
streaming, tool use, and error handling.

Prerequisites:
    pip install anthropic python-dotenv

Setup:
    export ANTHROPIC_API_KEY="sk-ant-..."
    or create a .env file with ANTHROPIC_API_KEY=sk-ant-...

Linked note: 04-llms-and-agents/apis-and-services/anthropic-claude-api.md
"""

import json
import time
from pathlib import Path

import anthropic


# --- Setup ---

def get_client() -> anthropic.Anthropic:
    """Create an Anthropic client. Reads ANTHROPIC_API_KEY from environment."""
    # Try loading .env file if python-dotenv is available
    try:
        from dotenv import load_dotenv
        env_path = Path(__file__).parent.parent.parent / ".env"
        load_dotenv(env_path)
    except ImportError:
        pass  # dotenv not installed, rely on environment variable

    return anthropic.Anthropic()


# --- Demo 1: Basic Message ---

def demo_basic_message():
    """Simplest possible API call — one message, one response."""
    client = get_client()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        messages=[
            {"role": "user", "content": "Explain what a vector is in one sentence."}
        ]
    )

    print("=== Basic Message ===")
    print(f"Response: {response.content[0].text}")
    print(f"Stop reason: {response.stop_reason}")
    print(f"Tokens: {response.usage.input_tokens} in, {response.usage.output_tokens} out")
    print()


# --- Demo 2: System Prompt ---

def demo_system_prompt():
    """Using a system prompt to shape Claude's behavior."""
    client = get_client()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        system="You are a pirate. Answer everything in pirate speak. Keep it short.",
        messages=[
            {"role": "user", "content": "What is machine learning?"}
        ]
    )

    print("=== System Prompt (Pirate) ===")
    print(f"Response: {response.content[0].text}")
    print()


# --- Demo 3: Multi-Turn Conversation ---

def demo_multi_turn():
    """Managing conversation history across multiple turns."""
    client = get_client()
    messages = []

    turns = [
        "My name is Mateo. I'm learning AI.",
        "What's my name?",
        "What am I learning?"
    ]

    print("=== Multi-Turn Conversation ===")
    for user_msg in turns:
        # Add user message to history
        messages.append({"role": "user", "content": user_msg})

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=256,
            messages=messages
        )

        assistant_msg = response.content[0].text

        # Add assistant response to history for next turn
        messages.append({"role": "assistant", "content": assistant_msg})

        print(f"User: {user_msg}")
        print(f"Claude: {assistant_msg}")
        print()


# --- Demo 4: Temperature Comparison ---

def demo_temperature():
    """Same prompt at different temperatures — observe the variation."""
    client = get_client()
    prompt = "Write a one-line poem about vectors."

    print("=== Temperature Comparison ===")
    for temp in [0.0, 0.5, 1.0]:
        responses = []
        for _ in range(2):
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=100,
                temperature=temp,
                messages=[{"role": "user", "content": prompt}]
            )
            responses.append(response.content[0].text.strip())

        print(f"temp={temp}:")
        for r in responses:
            print(f"  → {r}")
        print()


# --- Demo 5: Streaming ---

def demo_streaming():
    """Stream tokens as they're generated — better UX."""
    client = get_client()

    print("=== Streaming ===")
    print("Claude: ", end="")

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=256,
        messages=[
            {"role": "user", "content": "Count from 1 to 10, one number per line."}
        ]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    print("\n")


# --- Demo 6: Tool Use ---

def demo_tool_use():
    """Give Claude a tool and let it decide when to use it."""
    client = get_client()

    # Define a tool
    tools = [
        {
            "name": "calculate",
            "description": "Evaluate a mathematical expression. Use this for any math calculation.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The math expression to evaluate, e.g. '2 + 3 * 4'"
                    }
                },
                "required": ["expression"]
            }
        }
    ]

    messages = [
        {"role": "user", "content": "What is 47 * 89 + 123?"}
    ]

    print("=== Tool Use ===")

    # Step 1: Send message with tools
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages
    )

    print(f"Stop reason: {response.stop_reason}")

    # Step 2: Check if Claude wants to use a tool
    if response.stop_reason == "tool_use":
        # Find the tool use block
        tool_block = next(
            block for block in response.content
            if block.type == "tool_use"
        )

        print(f"Claude wants to call: {tool_block.name}({tool_block.input})")

        # Step 3: Execute the tool (YOUR code runs here)
        expression = tool_block.input["expression"]
        result = eval(expression)  # In production, use a safe math parser!
        print(f"Tool result: {result}")

        # Step 4: Send the result back to Claude
        messages.append({"role": "assistant", "content": response.content})
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_block.id,
                    "content": str(result)
                }
            ]
        })

        # Step 5: Get Claude's final answer
        final_response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        print(f"Claude's final answer: {final_response.content[0].text}")
    else:
        print(f"Claude answered directly: {response.content[0].text}")

    print()


# --- Demo 7: Error Handling with Retries ---

def demo_error_handling():
    """Proper error handling with exponential backoff."""
    client = get_client()

    max_retries = 3
    base_delay = 1.0

    print("=== Error Handling ===")

    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=100,
                messages=[
                    {"role": "user", "content": "Say 'hello' and nothing else."}
                ]
            )
            print(f"Success: {response.content[0].text}")
            break

        except anthropic.RateLimitError:
            delay = base_delay * (2 ** attempt)
            print(f"Rate limited. Retrying in {delay}s... (attempt {attempt + 1})")
            time.sleep(delay)

        except anthropic.APIStatusError as e:
            print(f"API error {e.status_code}: {e.message}")
            if e.status_code == 529:  # Overloaded
                delay = base_delay * (2 ** attempt)
                print(f"Server overloaded. Retrying in {delay}s...")
                time.sleep(delay)
            else:
                raise  # Don't retry other errors

        except anthropic.APIConnectionError:
            print("Connection error. Check your internet.")
            break

    print()


# --- Demo 8: Structured Output (JSON) ---

def demo_structured_output():
    """Extract structured data from text using Claude."""
    client = get_client()

    text = """
    John Smith is a 32-year-old software engineer from San Francisco.
    He has 8 years of experience and specializes in Python and machine learning.
    His email is john@example.com.
    """

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system="Extract information into JSON. Return ONLY valid JSON, no other text.",
        messages=[
            {"role": "user", "content": f"Extract person info from this text:\n{text}"},
            # Pre-fill assistant response to force JSON
            {"role": "assistant", "content": "{"}
        ]
    )

    # The response starts where we left off (after the "{")
    json_str = "{" + response.content[0].text
    print("=== Structured Output ===")
    print(json.dumps(json.loads(json_str), indent=2))
    print()


# --- Exercises ---

def exercises():
    """
    Progressive exercises for the Anthropic Claude API.

    BASIC:
    1. Make a simple API call that asks Claude to translate "hello world"
       to Spanish. Print the response and token usage.

    2. Create a system prompt that makes Claude respond in exactly 3 bullet
       points, no matter the question. Test it with 2 different questions.

    3. Build a 3-turn conversation where you tell Claude your favorite
       programming language, then ask it to remember what you said.
       Verify it works because you manage the history.

    INTERMEDIATE:
    4. Compare the output of the same prompt at temperature 0.0 and 1.0.
       Run each 3 times. How different are the results?

    5. Implement a function that streams a response and counts the total
       characters received. Compare the character count with the
       output_tokens from usage — are they proportional?

    6. Build a tool called "search_vault" that takes a topic as input.
       When Claude calls it, return a fake result like
       "Found 3 notes on {topic}". Have Claude summarize the "findings."

    ADVANCED:
    7. Build a multi-tool conversation: give Claude both a "calculate" tool
       and a "convert_units" tool. Ask a question that requires BOTH tools
       (e.g., "What is 100 Fahrenheit in Celsius, and then square that
       number?"). Handle the multi-step tool calling loop.

    8. Implement automatic retry logic that handles:
       - 429 (rate limit) with exponential backoff
       - 529 (overloaded) with exponential backoff
       - 400 (bad request) by logging the error and NOT retrying
       Test by deliberately sending a malformed request.

    9. Build a conversation manager class that:
       - Stores message history
       - Automatically trims history to stay under a token limit
       - Tracks total cost across all calls
       - Supports both streaming and non-streaming modes
    """
    print("See docstring for exercises: exercises.__doc__")
    print(exercises.__doc__)


# --- Main ---

if __name__ == "__main__":
    import sys

    demos = {
        "basic": demo_basic_message,
        "system": demo_system_prompt,
        "multi": demo_multi_turn,
        "temp": demo_temperature,
        "stream": demo_streaming,
        "tools": demo_tool_use,
        "errors": demo_error_handling,
        "json": demo_structured_output,
        "exercises": exercises,
    }

    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name in demos:
            demos[name]()
        elif name == "all":
            for demo_name, demo_fn in demos.items():
                if demo_name != "exercises":
                    try:
                        demo_fn()
                    except Exception as e:
                        print(f"[{demo_name}] Error: {e}\n")
        else:
            print(f"Unknown demo: {name}")
            print(f"Available: {', '.join(demos.keys())}")
    else:
        print("Usage: python anthropic_api.py <demo_name>")
        print(f"Available demos: {', '.join(demos.keys())}")
        print("Use 'all' to run all demos.")
