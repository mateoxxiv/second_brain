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
   - **Implement from scratch first** — raw Python/NumPy, no library shortcuts. Show what the abstraction hides. Optionally show the library version after for comparison.
   - Include a `if __name__ == "__main__":` block with demonstrations and printed output
   - Handle edge cases (zero vectors, singular matrices, empty inputs)

3. **Include exercises**: Every code file must have an `exercises()` function with progressive challenges:
   - **Basic** (2-3): Direct application, verify understanding of the operation
   - **Intermediate** (2-3): Combine concepts, solve problems, connect to ML use cases
   - **Advanced** (1-2): Edge cases, proofs-by-code, optimizations, "why does this break when..."
   - Each exercise should include a clear problem statement as a docstring/comment
   - Include expected outputs or assertions so the user can verify correctness

4. **Link it**: If a corresponding note exists, update that note to link to this code file in its Code Example section.

5. **Show the code**: Display the full file to the user for review before committing.

6. **After approval**: Commit the code file (and updated note if applicable).

7. **Explain**: Briefly walk through the implementation highlighting key design decisions and any trade-offs made.
