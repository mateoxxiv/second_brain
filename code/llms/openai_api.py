"""
OpenAI API — Runnable Examples and Exercises

Demonstrates core OpenAI API features:
- Basic message, system prompts, multi-turn conversations
- Temperature control, streaming, structured output
- Tool use (function calling), error handling

Prerequisites:
  pip install openai
  export OPENAI_API_KEY="sk-..."

Usage:
  python openai_api.py basic_message
  python openai_api.py all
"""

import json
import sys
from openai import OpenAI


# --- Demo Functions ---


def basic_message() -> None:
    """Send a simple message and print the response."""
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "What is a vector in one sentence?"}],
    )
    print("Response:", response.choices[0].message.content)
    print(f"Tokens: {response.usage.prompt_tokens} in, {response.usage.completion_tokens} out")


def system_prompt() -> None:
    """Use a system prompt to shape behavior."""
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You are a pirate. Answer everything in pirate speak."},
            {"role": "user", "content": "What is machine learning?"},
        ],
    )
    print("Pirate:", response.choices[0].message.content)


def multi_turn() -> None:
    """Demonstrate multi-turn conversation (stateless — send full history)."""
    client = OpenAI()
    messages: list[dict] = [
        {"role": "system", "content": "You are a math tutor. Be concise."},
        {"role": "user", "content": "What is a dot product?"},
    ]

    # Turn 1
    r1 = client.chat.completions.create(model="gpt-5-mini", messages=messages)
    assistant_msg = r1.choices[0].message.content
    print("Turn 1:", assistant_msg)

    # Turn 2 — append history
    messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": "Give me a numeric example."})

    r2 = client.chat.completions.create(model="gpt-5-mini", messages=messages)
    print("Turn 2:", r2.choices[0].message.content)


def temperature_demo() -> None:
    """Compare low vs high temperature outputs."""
    client = OpenAI()
    prompt = "Give me a creative name for a coffee shop."

    for temp in [0.0, 1.0, 1.5]:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            temperature=temp,
            messages=[{"role": "user", "content": prompt}],
        )
        print(f"temp={temp}: {response.choices[0].message.content}")


def streaming() -> None:
    """Stream tokens as they are generated."""
    client = OpenAI()
    stream = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "Count from 1 to 10, one per line."}],
        stream=True,
    )
    print("Streaming: ", end="")
    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)
    print()


def tool_use() -> None:
    """Demonstrate function calling (tool use)."""
    client = OpenAI()

    # Define the tool
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather for a city",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name"},
                    },
                    "required": ["city"],
                },
            },
        }
    ]

    messages = [{"role": "user", "content": "What's the weather in Bogota?"}]

    # Step 1: Model decides to call the tool
    response = client.chat.completions.create(
        model="gpt-5-mini", messages=messages, tools=tools
    )

    msg = response.choices[0].message
    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_call.function.name}({args})")

        # Step 2: Simulate executing the function
        weather_result = json.dumps({"city": args["city"], "temp": 18, "condition": "rainy"})

        # Step 3: Send result back
        messages.append(msg)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": weather_result,
        })

        # Step 4: Get final response
        final = client.chat.completions.create(
            model="gpt-5-mini", messages=messages, tools=tools
        )
        print("Final:", final.choices[0].message.content)


def structured_output() -> None:
    """Demonstrate structured output with strict JSON schema."""
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "Extract: 'John is 30 years old and lives in NYC'"}],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "person_info",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"},
                        "city": {"type": "string"},
                    },
                    "required": ["name", "age", "city"],
                    "additionalProperties": False,
                },
            },
        },
    )
    data = json.loads(response.choices[0].message.content)
    print(f"Extracted: {data}")


def error_handling() -> None:
    """Demonstrate proper error handling."""
    from openai import (
        APIConnectionError,
        AuthenticationError,
        RateLimitError,
    )

    client = OpenAI()

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": "Hello!"}],
        )
        print("Success:", response.choices[0].message.content)
    except AuthenticationError:
        print("ERROR: Invalid API key. Check OPENAI_API_KEY.")
    except RateLimitError:
        print("ERROR: Rate limit hit. Retry with exponential backoff.")
    except APIConnectionError:
        print("ERROR: Cannot connect to OpenAI. Check your network.")


# --- Exercises ---


def exercises() -> None:
    """
    Progressive exercises to practice the OpenAI API.

    BASIC:
    1. Send a message asking Claude to translate "hello world" to 3 languages.
       Expected: A response with translations in 3 languages.

    2. Create a system prompt that makes the model respond only in bullet points.
       Test with: "Explain gradient descent"
       Expected: Response formatted entirely as bullet points.

    3. Build a 3-turn conversation where you ask about a topic, ask for an
       example, then ask it to explain like you're 5.
       Expected: Each turn builds on the previous context.

    INTERMEDIATE:
    4. Compare outputs of the same prompt at temperatures 0.0, 1.0, and 2.0.
       Prompt: "Invent a name for a new programming language"
       Run each 3 times. Expected: temp 0 gives same answer, temp 2 varies wildly.

    5. Define a tool called `calculate` that takes an expression string and
       returns the result. Have the model use it to solve: "What is 15% of 847?"
       Expected: Model calls calculate("847 * 0.15") → returns 127.05

    6. Use structured output (strict JSON schema) to extract from a paragraph:
       - All person names (list of strings)
       - All locations (list of strings)
       - Sentiment (positive/negative/neutral)
       Expected: Valid JSON matching your schema exactly.

    ADVANCED:
    7. Build a multi-tool agent that has access to:
       - get_weather(city) -> weather info
       - search_web(query) -> search results
       - calculate(expr) -> math result
       Have it answer: "What's 20% of the temperature in Tokyo right now?"
       Expected: Model chains tool calls (get_weather → calculate).

    8. Implement exponential backoff retry logic for rate-limited requests.
       Simulate by making rapid requests. Expected: Graceful retry with
       increasing delays (1s, 2s, 4s, 8s max).

    9. Build a ConversationManager class that:
       - Manages message history
       - Supports system prompt changes mid-conversation
       - Tracks total token usage across all turns
       - Has a cost_so_far() method that estimates $ spent
       Expected: Clean API, accurate token tracking.
    """
    print("See the docstring for exercises. Edit this file to implement them!")
    print("Start with exercise 1 (basic) and work your way up.")


# --- CLI Runner ---

DEMOS = {
    "basic_message": basic_message,
    "system_prompt": system_prompt,
    "multi_turn": multi_turn,
    "temperature": temperature_demo,
    "streaming": streaming,
    "tool_use": tool_use,
    "structured_output": structured_output,
    "error_handling": error_handling,
    "exercises": exercises,
}


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python openai_api.py <demo_name>")
        print(f"Available: {', '.join(DEMOS.keys())}, all")
        return

    name = sys.argv[1]
    if name == "all":
        for demo_name, func in DEMOS.items():
            if demo_name == "exercises":
                continue
            print(f"\n{'='*50}")
            print(f"  {demo_name}")
            print(f"{'='*50}")
            func()
    elif name in DEMOS:
        DEMOS[name]()
    else:
        print(f"Unknown demo: {name}")
        print(f"Available: {', '.join(DEMOS.keys())}, all")


if __name__ == "__main__":
    main()
