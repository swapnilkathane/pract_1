vowels="aeiou"
ip_str="Swapnil is good boy"
ip_str=ip_str.casefold()
count={}.fromkeys(vowels,0)
print(count)
for x in ip_str:
    if x in count:
        count[x]+=1
print(count)