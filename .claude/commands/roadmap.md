Generate or update the study roadmap based on current vault state.

Optional focus: $ARGUMENTS

Follow these steps:

1. **Audit the vault**: Scan all folders and notes. Count notes per area, check their status tags (seed/growing/evergreen), and identify coverage gaps.

2. **Assess progress** for each area:
   - 01-foundations: linear algebra, calculus, probability, algorithms, databases
   - 02-machine-learning: supervised, unsupervised, ensemble, features, evaluation
   - 03-deep-learning: fundamentals, CNNs, RNNs, transformers, training
   - 04-llms-and-agents: architectures, fine-tuning, RAG, prompting, agents
   - 05-mlops: deployment, monitoring, CI/CD, infrastructure

3. **Generate the roadmap**:
   - What's been covered (with note counts and quality)
   - What's in progress
   - What's missing
   - **Recommended next steps**: Ordered list of topics to study next, considering prerequisites (e.g., linear algebra before neural networks)
   - Estimated scope for each topic (how many notes/code files it would take)

4. **Save or update**: Write/update the roadmap as `07-resources/study-roadmap.md`. Show it to the user before committing.

5. **Suggest a study session**: Based on the roadmap, recommend what to work on next and offer to start a `/session` on that topic.
