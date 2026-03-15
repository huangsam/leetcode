# LeetCode Agent Guidelines

When working on `python/` files:
- Add problem URL to the first line: `# https://leetcode.com/problems/...`
- Use type hints for function parameters and return types
- Add docstring explaining the approach
- Add time/space complexity comments
- Test solution with python interpreter before committing

When working on `java/solution/` files:
- Add problem URL to the first line: `// https://leetcode.com/problems/...`
- Add JavaDoc for public methods explaining the approach
- Add time/space complexity comments
- Test solution with jshell interpreter before committing

When adding new solutions:
- Run `python leetc.py sync` to update `problems.json` and `SOLUTIONS.md`

When suggesting new problems to solve:
- Look at what has been solved in `problems.json`
- Check for popular problems that are not yet solved
- Consider problems that cover areas that have less coverage
