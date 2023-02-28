import streamlit as st

st.title("Innomatics Data App")
st.header('Hai all !! This is Sravanthi..Welcome to my page..!')
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()