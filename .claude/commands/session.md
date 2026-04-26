Start a focused study session on: $ARGUMENTS

If no topic is given, check the roadmap at `07-resources/study-roadmap.md` and suggest the next logical topic.

A study session combines multiple workflows into one guided flow. This vault follows a DEEP-FIRST approach — we derive, prove, implement from scratch, and exercise until mastery.

1. **Introduction** (2 min read):
   - Briefly explain what the topic is and why it matters in the AI/ML landscape
   - State prerequisites — check if those notes exist in the vault, warn if gaps
   - Outline what we'll cover in this session

2. **Concept explanation** (deep, not surface):
   - Explain the core concept clearly, building from first principles
   - Include mathematical derivations — don't just state formulas, show where they come from
   - Use LaTeX notation for all math
   - Include diagrams (Mermaid) when visual explanation helps
   - Connect to concepts the user already has notes on
   - Explain the intuition AND the rigor

3. **Reference existing notes**:
   - Search the vault for notes already covering this topic or prerequisites
   - List the relevant notes found and briefly state what each covers
   - Identify any gaps — concepts not yet in the vault that this session should eventually produce
   - Do NOT create notes during the session; note creation happens separately via `/note`
   - When referencing what a future note should look like, it uses the layered structure: TL;DR → Intuition → Mechanics → In ML → Exercises

4. **Code implementation**:
   - Build a from-scratch implementation (raw Python/NumPy first, no library shortcuts)
   - Walk through the code step by step, explaining design decisions
   - Include an `exercises()` function with progressive challenges:
     - Basic: direct application of the concept
     - Intermediate: combine concepts, non-trivial problems
     - Advanced: edge cases, optimizations, "prove this property in code"
   - Show the code for review before saving

5. **Knowledge check** (5-7 questions, adaptive):
   - Start with a warm-up question
   - Increase difficulty based on answers
   - Mix types: conceptual, mathematical derivation, code-based, "what would happen if...", debugging
   - Use Socratic method — don't give answers, guide with hints
   - If the user struggles, break it down further before moving on

6. **Wrap up**:
   - Summarize what was learned
   - Identify any remaining gaps honestly
   - Update the roadmap if it exists
   - Suggest the next topic for the following session
   - Commit all approved files

7. **Resource recommendations**: Always end with at least:
   - 1 foundational resource (textbook chapter or lecture)
   - 1 practical resource (blog post or tutorial with exercises)
   - 1 advanced resource (paper or proof-heavy reference)
