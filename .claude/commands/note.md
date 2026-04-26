Create an atomic permanent note on the topic: $ARGUMENTS

Follow these steps:

1. **Research**: Search the vault for existing related notes using Glob and Grep. Understand what already exists to avoid duplication and to find linking opportunities.

2. **Scope check**: Ensure the topic is truly atomic (one concept). If it's too broad, tell the user and suggest how to split it. Examples of good splits:
   - "Vectors" is too broad → split into: "Vectors and Vector Spaces" (theory), "Vector Operations" (operations + worked examples), "Vectors in ML" (applications)
   - "Gradient Descent" is okay — one concept
   - "Optimization" is too broad → split into: "Gradient Descent", "Learning Rate", "Convexity", etc.

3. **Write the note**: Use the permanent note template from `templates/permanent-note.md`. Follow these rules:
   - No H1 title — the filename IS the title in Obsidian
   - One concept only — max ~70 lines
   - All metadata (tags, related, sources, domain) in the YAML frontmatter block. Nothing inline.
   - **TL;DR**: one sentence at the top — the single most important thing to remember
   - **Intuition**: plain English and analogy before any math
   - **Mechanics**: formal definition + derivation (show where formulas come from) + properties table + short code snippet (< 20 lines)
   - **In ML**: 2–3 bold-labeled paragraphs connecting to real algorithms or systems
   - **Exercises**: basic / intermediate / advanced — required, not optional
   - Link to existing vault notes using `[[wikilinks]]` — never plain text references
   - Tag as `status/seed`
   - Place in the correct subfolder based on the topic

4. **Code file**: If the concept benefits from a runnable implementation, create a `.py` file in the corresponding `code/` subfolder with progressive exercises (basic → intermediate → advanced). Link it from the note.

5. **Show the note**: Display the full note content to the user for review. Do NOT commit yet.

6. **Wait for feedback**: Only commit after the user approves or requests changes.

7. **Recommend**: After the note is finalized, suggest:
   - 2-3 related topics that would make good follow-up notes
   - Learning resources: textbooks, lectures, papers, blog posts, videos
