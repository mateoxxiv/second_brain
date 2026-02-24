Generate a comprehensive overview of the vault's current state.

Follow these steps:

1. **Count notes** by folder and subfolder. Distinguish between permanent notes, literature notes, and project notes.

2. **Status distribution**: Count notes by tag:
   - #status/seed — just started
   - #status/growing — in development
   - #status/evergreen — mature and complete

3. **Orphan analysis**: Find notes with no incoming links (nothing links to them) and notes with no outgoing links (they don't link to anything).

4. **Code coverage**: How many notes have corresponding code files in `code/`? Which concepts are missing implementations?

5. **Recent activity**: Show the most recently created/modified notes (based on git history).

6. **Health metrics**:
   - Average links per note
   - Folders with zero notes (knowledge gaps)
   - Seed notes older than 2 weeks (stale seeds that need attention)

7. **Present as a dashboard**:
   ```
   Vault Status — [date]
   ========================
   Total notes: X (Y seed | Z growing | W evergreen)
   ...
   ```

8. **Recommend actions**: Based on the status, suggest 3 concrete next actions (e.g., "Promote 'Gradient Descent' from seed to growing — it needs a code example").
