def fun(s):
 import re
 if(re.search(r"^[\w,-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$",s)):
    return True
 else:
   return False

def filter_mail(emails):
    return list(filter(fun, emails))

if _name_ == '_main_':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
