# LeetCode

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/huangsam/leetcode/ci.yml)](https://github.com/huangsam/leetcode/actions)

Python / Java solutions for [LeetCode problems](https://leetcode.com/).

🐍 🐍 🐍 - 🏃‍♂️ 🏃‍♂️ 🏃‍♂️ - ☕ ☕ ☕

The URL of each solution is embedded at the top of the file.

Run `bash urls.sh` to see the URLs for all attempted problems.

## Validation

For Python solutions:

```shell
virtualenv venv # setup starts here
source venv/bin/activate
pip install -r requirements.txt
ruff check python # validation starts here
mypy python
```

For Java solutions:

```shell
gradle build # validation starts here
```
