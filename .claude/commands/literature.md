Create a literature note from: $ARGUMENTS

The argument can be a URL, a paper title, or a topic to search for.

Follow these steps:

1. **Fetch the source**:
   - If a URL is provided, use WebFetch to read the content
   - If a paper/article title is given, use WebSearch to find it, then fetch
   - If a general topic is given, search for the best recent resource on it

2. **Create the literature note**: Use the template from `templates/literature-note.md`:
   - Fill in source URL, type (paper/blog/video/course/documentation), and date
   - Write a clear summary in your own words (not copy-paste)
   - Extract 3-5 key takeaways
   - Add your analysis in "My Thoughts" — why this matters, how it connects to AI/ML mastery
   - Save in `07-resources/`

3. **Identify permanent notes**: From the key takeaways, identify 1-3 atomic concepts that deserve their own permanent notes. List them in "Permanent Notes Created" section as links (even if they don't exist yet — they become future work).

4. **Show the note**: Display the full content to the user for review before committing.

5. **After approval**: Commit the literature note. Ask if the user wants to create any of the identified permanent notes now.
