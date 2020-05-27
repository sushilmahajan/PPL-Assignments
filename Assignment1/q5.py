pages = []
missing = []
ip = 0
print("Enter available pages, type -1 to terminate")

ip = int(input())
while ip != -1:
    pages.append(ip)
    ip = int(input())

for x in range(1, 26):
    if x not in pages :
        missing.append(x)

print("Missing Pages:", missing)

