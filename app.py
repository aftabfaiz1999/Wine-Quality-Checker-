import streamlit as st
import pickle
import base64
import warnings


with warnings.catch_warnings():
      warnings.simplefilter("ignore", category=UserWarning)
model = pickle.load(open('model','rb'))



def main():

    st.title('Alcohol Quality')
    
    fixed_acidity=st.text_input('fixed acidity')
    volatile_acidity=st.text_input('volatile acidity')
    citric_acid=st.text_input('citric acid')
    residual_sugar=st.text_input('residual sugar')
    chlorides=st.text_input('chlorides')
    free_sulfur_dioxide=st.text_input('free sulfur dioxide')
    total_sulfur_dioxide=st.text_input('total sulfur dioxide')
    density=st.text_input('density')
    pH=st.text_input('pH')
    sulphates=st.text_input('sulphates')
    alcohol=st.text_input('alcohol')
    
    if st.button('Predict'):
        makepred=model.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])
        
        if makepred[0]==5:
            good='Quality is Best 5'
        else:
            good='Quality is Just Good 6'
        st.success(good)
        
        
    link = '[GitHub](https://github.com/aftabfaiz1999)'
    st.markdown(link, unsafe_allow_html=True)
    
    link = '[Linkedin](https://www.linkedin.com/in/aaftab-shaikh-a283a1165/)'
    st.markdown(link, unsafe_allow_html=True)
    
if __name__=='__main__':
    main()   
