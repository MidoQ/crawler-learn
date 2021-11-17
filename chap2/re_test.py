"""使用正则表达式"""
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
re_str = '^Hello\s\d\d\d\s\d{4}\s\w{10}'
result = re.match(re_str, content)
print(result)
print(result.group())
print(result.span())
