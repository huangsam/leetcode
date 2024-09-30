# LeetCode

![GitHub actions](https://github.com/huangsam/leetcode/actions/workflows/ci.yml/badge.svg)

Python / Java Solutions of [LeetCode Questions](https://leetcode.com/).

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
mvn install # validation starts here
```
