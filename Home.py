import streamlit as st
from PIL import Image
import inflection
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Home",layout="wide",initial_sidebar_state="expanded",page_icon="🏡")

COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
@st.cache_data
def country_name(country_id):
    return COUNTRIES[country_id]

@st.cache_data
def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
@st.cache_data
def color_name(color_code):
    return COLORS[color_code]

@st.cache_data
def rename_columns():
    df = pd.read_parquet("datasets/zomato.parquet")
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def folium_map():
    map_ = folium.Map(location = [4.653079918274051, 19.423828125000004],
                  tiles= 'Cartodbpositron',
                  zoom_start=2)
    markerCluster = MarkerCluster().add_to(map_)

    for i, row in df1.iterrows():
        lat = df1.at[i,'latitude']
        lng = df1.at[i,'longitude']
        color = df1.at[i, 'rating_color']
        nota = df1.at[i,'aggregate_rating']
        iframe = folium.IFrame(( str(df1.at[i,'restaurant_name']) + '<br>' + 
                                'Tipo de comida: '+ str(df1.at[i, 'cuisines']) + '<br>' + 
                                'Nota Média: '+ str(df1.at[i, 'aggregate_rating']) + '<br>'+
                                'Preço de um prato para dois: R$' + str(df1.at[i, 'average_cost_for_two'])))
        popup = folium.Popup(iframe, min_width=250, max_width=300)
        icon = folium.Icon(color=color, prefix = 'fa', icon = 'home')
        if nota >= 4.5:
            color = 'darkgreen'
        elif (nota < 4.5) & (nota >= 4):
            color = 'green'
        elif (nota < 4) & (nota >= 3.5):
            color = 'lightgreen'
        elif (nota < 3.5) & (nota >= 3):
            color = 'orange'
        elif (nota < 3) & (nota >= 2.5):
            color = 'red'
        elif (nota < 2.5) & (nota >= 2):
            color = 'darkred'
        else:
            color = 'darkred'
        folium.Marker(location=[lat, lng],
                      icon=icon, popup=popup).add_to(markerCluster)

    folium.TileLayer('OpenStreetMap').add_to(map_)
    folium.TileLayer('cartodbpositron').add_to(map_)
    folium.LayerControl().add_to(map_)
    return folium_static(map_, width=1080, height=600)

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df1 = rename_columns()
df1['rating_color'] = df1['rating_color'].map(color_name)
df1['country_code'] = df1['country_code'].map(country_name)
df1['price_range'] = df1['price_range'].map(create_price_type)
df1 = df1.dropna(subset=['cuisines'])
df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

df_download = convert_for_download(df1)

image_path = "assets/logo1.png"
image = Image.open(image_path)
st.sidebar.image(image, width = 120)
st.sidebar.write("## Filtros")
paises = st.sidebar.multiselect("Escolha os Paises que \n Deseja visualizar os Restaurantes", 
                                options=df1['country_code'].unique(), 
                                default=["Brazil", "United States of America", "England", "Australia"])
st.sidebar.write("### Baixe a base de dados tratada:")
st.sidebar.download_button("Download", 
                           data= df_download, 
                           file_name='dados_zomato_tratados.csv',
                             mime="text/csv",use_container_width=True)

paises_selecionados = df1['country_code'].isin(paises)
df1 = df1.loc[paises_selecionados, :].copy()

st.write('# Fome Zero!')
st.write('## O Melhor lugar para encontrar seu mais novo restaurante favorito!')
st.write('### Temos as seguintes marcas dentro da nossa plataforma:')

with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Restaurantes Cadastrados", value=df1['restaurant_id'].nunique())
        with col2:
            st.metric("Países Cadastrados", value=df1['country_code'].nunique())
        with col3:
            st.metric("Cidades Cadastrados", value=df1['city'].nunique())
        with col4:
            st.metric("Avaliações Feitas", value=df1['votes'].sum())
        with col5:
            st.metric("Tipos de Culinárias", value=df1['cuisines'].nunique())
with st.container():
    folium_map()#folium_static(map_, width=1080, height=600)
