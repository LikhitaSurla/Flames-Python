import streamlit as st
st.title("Welcome to the page")
l=['Friends','Lovers','Attraction','Marriage','Enemies',"Siblings"]
a=st.text_input('Enter First name')
b=st.text_input('Enter Second name')
a=list(a)
b=list(b)

count=0
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]==b[j]):
            print(a[i],b[j])
            b[j]=2
            count=count+2
a.extend(b)
x=len(a)
diff=x-count



while(len(l)>1):
    k=(diff%len(l)-1)
    if k>=0:
        l = l[k+1:] + l[:k]
    else:
        l=l[:len(l)-1] 

if st.button('Submit'):
    st.success(l[0])
    
