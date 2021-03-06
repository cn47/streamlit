import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

from multiapp import MultiApp

st.set_page_config(page_title='Sample App!!',
                   page_icon="π¦",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   )



data_csv = './data/newly_confirmed_cases_daily.csv'
df = pd.read_csv(data_csv)
df['Date'] = pd.to_datetime(df.Date)

### Define Process #############################################################
def main():
    app = MultiApp()
    app.add_app('η»ε1', γγγ·γ)
    app.add_app('η»ε2', γγγ)
    app.add_app("γ³γ­γDF-ζ±δΊ¬/εζ΅·ι/ε€§ιͺ", corona_positive_dataframe)
    app.add_app("γ³γ­γη·γ°γ©γ-ζ±δΊ¬/εζ΅·ι/ε€§ιͺ", corona_positive_line)
    app.add_app("γ³γ­γζ£εΈε³-ζ±δΊ¬/ε€§ιͺ", corona_positive_scatter)
    app.run()


### Define Function ############################################################
def γγγ·γ():
    img='./data/Screenshot_20220120-005008999.jpg'
    caption='ozex'
    image = Image.open(img)
    st.image(image, caption=caption ,use_column_width=True)
def γγγ():
    img='./data/Screenshot_20220212-084733242.jpg'
    caption='mole'
    image = Image.open(img)
    st.image(image, caption=caption ,use_column_width=True)

###
def corona_positive_dataframe():
    st.dataframe(df.iloc[:,0:], width=None, height=700)

###
def corona_positive_line():
    with st.echo(code_location='below'):
        st.line_chart(df[['Tokyo', 'Hokkaido', 'Osaka']], width=150, height=700)

###
def corona_positive_scatter():
    with st.echo(code_location='below'):
        fig = px.scatter(x=df.Date, y=df.Tokyo)
        fig.add_scatter(x=df.Date, y=df.Osaka, mode='markers')
        fig.update_layout(xaxis_title='ζ₯δ»',
                          yaxis_title='ι½ιεΊη',
                          font_size=15, hoverlabel_font_size=20, width=1000, height=700)
        st.write(fig)


### Execute Process ############################################################
if __name__ == '__main__':
    main()
