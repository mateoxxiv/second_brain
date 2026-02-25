Start a quiz on: $ARGUMENTS

If no topic is given, pick a topic based on recent notes or areas that need reinforcement.

Rules:

1. **Start by assessing**: Ask 1 warm-up question to gauge current understanding of the topic.

2. **Adapt dynamically**:
   - If the user answers correctly and confidently → increase difficulty, go deeper, ask edge cases, ask for derivations
   - If the user struggles → step back, break the concept down, give hints before revealing answers
   - Mix question types:
     - **Conceptual**: "Explain in your own words why..."
     - **Mathematical**: "Derive...", "Prove that...", "Compute step by step..."
     - **Code-based**: "What does this code output?", "Find the bug", "Implement X"
     - **Scenario**: "What would happen if...", "Compare X vs Y"
     - **Edge cases**: "What breaks when...", "Why doesn't this work for..."
     - **Teach-back**: "Explain this to a junior engineer"

3. **Socratic method**: Don't just say "wrong." Ask follow-up questions that guide the user toward the correct answer. Only explain directly if they're stuck after 2-3 hints.

4. **Require work**: For math questions, ask the user to show their steps, not just the final answer. For code questions, ask them to trace execution mentally.

5. **After each answer**: Briefly explain why the correct answer is correct, and connect it to the bigger picture.

6. **Track progress**: After 5-7 questions, give a summary:
   - Topics where understanding is solid
   - Topics that need more review
   - Suggest specific notes to revisit or create
   - Recommend exercises from code files to practice

7. **Reference the vault**: When relevant, point to existing notes with [[wikilinks]] or suggest creating new ones for concepts the user struggled with.

8. **Keep it engaging**: Vary the format. Challenge the user. An architect must be able to think on their feet.
