import re
a="admin 011"
b="aa admin 12"

print(re.match("^admin.*",a))
print(re.match("^admin.*",b))
