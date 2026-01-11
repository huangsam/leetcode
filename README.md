# LeetCode

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/leetcode/ci.yml)](https://github.com/huangsam/leetcode/actions)

Python / Java solutions for [LeetCode problems](https://leetcode.com/). 🚀

Sharpen your coding skills with these solutions—feel free to explore, learn, and contribute!

🐍 🐍 🐍 - 🏃‍♂️ 🏃‍♂️ 🏃‍♂️ - ☕ ☕ ☕

The URL of each solution is embedded at the top of the file.

Run `uv run python leetc.py urls` to see the URLs for all attempted problems.

## Getting started

To validate Python solutions:

```shell
uv run ruff check python
uv run mypy python
```

To validate Java solutions:

```shell
gradle build
```

### CLI tool for LeetCode

To get details on problems and progress without visiting the website, use the `leetc` CLI tool:

```shell
# List URLs for all solutions in the repository
uv run leetc.py urls

# Get details for a specific problem
uv run leetc.py detail $URL_FRAGMENT

# Get your overall progress summary
uv run leetc.py progress $USERNAME
```

## Additional resources

These resources can complement learning via LeetCode:

- 🎓 [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university)
- 📚 [thealgorithms](https://github.com/thealgorithms)
- 🤝 [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook)
- 🏛️ [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)
- 🏗️ [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning)
- 🛠️ [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
- 🗺️ [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap)
