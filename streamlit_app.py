import streamlit as st
from utils import load_data, calculate_ai_index

st.set_page_config(page_title="Keiba AI指数アプリ v8", layout="wide")
st.title("🏇 Keiba AI指数アプリ v8")
st.write("出馬表URLを選択・自動取得し、AI指数と過去走比較を表示します。")

url = st.text_input("出馬表URLを入力してください（netkeiba）:")
if url:
    df = load_data(url)
    if df is not None:
        df["AI指数"] = df.apply(calculate_ai_index, axis=1)
        st.dataframe(df)
    else:
        st.warning("データを取得できませんでした。")
