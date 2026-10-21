import streamlit as st

st.set_page_config(page_title="荷兰豆勇闯蛋仔", page_icon="🥚", layout="wide")

st.title("🥚 荷兰豆勇闯蛋仔 水彩风小游戏")
st.markdown("点击屏幕或按空格键跳跃，躲开彩色蛋仔，挑战最高分~")

# 直接嵌套本地HTML游戏文件 自动占满页面
with open("新建文件夹（2）/egg_run_game.html", "r", encoding="utf-8") as f:
    game_html = f.read()

st.components.v1.html(game_html, height=600, scrolling=False)
