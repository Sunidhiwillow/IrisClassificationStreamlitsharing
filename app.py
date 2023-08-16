

st.title("StreamlitDeployment")
html_temp = """
<div_style ="background-color:teal ;padding:10px">
<h2 style ="color:white text-align:centre;">Iris Classification</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html = True)
activities = ['logistic Regression', 'KNN', 'DecisionTree']
option = st.sidebar.selectbox("Which model would you like to use?", activities)
st.subheader(option)
st.spinner("Hello")
sepal_length = st.slider('Select sepal length', 0.0,10.0)
sepal_width = st.slider('Select sepal width', 0.0,10.0)
petal_length = st.slider('Select petal length', 0.0,10.0)
petal_width = st.slider('Select petal width', 0.0,10.0)
input = np.array([[sepal_length, sepal_width,petal_length,petal_width]])
if st.button('Classify'):
  if option=='logistic Regression':
    st.success(classify((model1.predict(input))))
  elif option =='KNN':
    st.success(classify((model2.predict(input))))
  else:
    st.success(classify((model3.predict(input))))
