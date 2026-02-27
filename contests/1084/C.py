t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    st = []
    for c in s:
        if st and st[-1] == c:
            st.pop()
        else:
            st.append(c)
            
    if not st:
        print("YES")
    else:
        print("NO")
