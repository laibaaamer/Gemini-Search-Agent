import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from ddgs import DDGS
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Put it in your .env file.")
client = genai.Client(api_key=api_key)
MODEL = "gemini-3.6-flash"
MAX_STEPS = 5  
def search(query: str) -> dict:
    """Search the live web and return the top results."""
    print(f"\n[TOOL EXECUTION] search(query={query!r})")
    try:
        results = DDGS().text(query, max_results=5)
        formatted = [
            {
                "title": r.get("title", ""),
                "url": r.get("href", ""),
                "snippet": r.get("body", ""),
            }
            for r in results
        ]
        print(f"[TOOL RESULT] {len(formatted)} results found.")
        return {"query": query, "results": formatted}
    except Exception as e:
        print(f"[TOOL ERROR] {e}")
        return {"query": query, "error": str(e)}
TOOL_IMPLEMENTATIONS = {"search": search}
search_declaration = types.FunctionDeclaration(
    name="search",
    description=(
        "Search the live web for current or up-to-date information. "
        "Use this whenever the user asks about recent news, current events, "
        "or anything that may have changed recently."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "query": types.Schema(
                type=types.Type.STRING,
                description="The search query to send to the web.",
            )
        },
        required=["query"],
    ),
)
config = types.GenerateContentConfig(
    tools=[types.Tool(function_declarations=[search_declaration])],
    # We run the tool loop ourselves so we can print each step.
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    system_instruction=(
        "You are a helpful research assistant. When you use the search tool, "
        "base your answer on the results and cite the source URLs."
    ),
)
def ask_agent(question: str) -> str:
    contents = [
        types.Content(role="user", parts=[types.Part(text=question)])
    ]
    for step in range(MAX_STEPS):
        print(f"\n[AGENT] Thinking (step {step + 1})...")
        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=config,
        )
        candidate = response.candidates[0]
        contents.append(candidate.content)
        function_calls = [
            part.function_call
            for part in (candidate.content.parts or [])
            if part.function_call
        ]
        if not function_calls:
            print("[AGENT] Done - no more tools needed.")
            return response.text or "(the model returned no text)"
        result_parts = []
        for call in function_calls:
            print(f"[AGENT DECISION] Calling tool: {call.name}({dict(call.args)})")
            impl = TOOL_IMPLEMENTATIONS.get(call.name)
            if impl is None:
                result = {"error": f"Unknown tool: {call.name}"}
            else:
                result = impl(**dict(call.args))
            print("[SEARCH RESULTS]")
            print(json.dumps(result, indent=2, ensure_ascii=False)[:1500])
            result_parts.append(
                types.Part.from_function_response(
                    name=call.name,
                    response={"result": result},
                )
            )
        contents.append(types.Content(role="user", parts=result_parts))
    return "Stopped: the agent hit the maximum number of tool-calling steps."
if __name__ == "__main__":
    print("=== Gemini Web Search Agent ===")
    question = input("Ask your question: ").strip()
    if not question:
        raise SystemExit("No question given.")
    print(f"\n[USER] {question}")
    answer = ask_agent(question)
    print("\n[FINAL RESPONSE]")
    print(answer)