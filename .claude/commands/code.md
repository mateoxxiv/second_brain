Generate a runnable Python implementation for: $ARGUMENTS

Follow these steps:

1. **Check context**: Search the vault for existing notes on this topic. The code should complement the conceptual note, not replace it.

2. **Write the code file**:
   - Place in the appropriate `code/` subfolder (foundations, ml, dl, llms, or projects)
   - Include a docstring at the top explaining what the file demonstrates
   - Use type hints on function signatures
   - Keep it self-contained and runnable with `python filename.py`
   - Use minimal dependencies (prefer stdlib + numpy/scipy/sklearn)
   - Add inline comments explaining the "why", not the "what"
   - If it's an algorithm, implement it from scratch first, then optionally show the library version
   - Include a `if __name__ == "__main__":` block with example usage and output

3. **Link it**: If a corresponding note exists, update that note to link to this code file in its Code Example section.

4. **Show the code**: Display the full file to the user for review before committing.

5. **After approval**: Commit the code file (and updated note if applicable).

6. **Explain**: Briefly walk through the implementation highlighting key design decisions and any trade-offs made.
