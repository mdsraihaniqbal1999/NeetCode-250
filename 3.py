def check_anagram(s,t):
    if len(s)!= len(t):
        return False
    count_s = [0] * 26
    count_t = [0] * 26
    
    for char in s:
        count_s[ord(char)-ord('a')]+= 1 
    
    for char in t:
        count_t[ord(char)-ord('a')]+= 1
 
    return count_s == count_t
    
s= input("enter the string1: ")
t= input("enter the string2: ")
print(f"String 1: {s}")
print(f"String 1: {t}")

res = check_anagram(s,t)
print(f"The is an anagram: {res}")
