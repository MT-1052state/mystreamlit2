import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ページレイアウトを2カラムに設定
st.set_page_config(layout="wide")

# タイトル
st.title('Marketing Automation ツール')

# 2カラムレイアウトの作成
left_column, right_column = st.columns([1, 2])

# 左カラム: Snowflake接続情報
with left_column:
    st.header("Snowflake接続設定")
    
    # 接続情報入力エリア
    account = st.text_input("アカウント名", placeholder="例: your_account")
    user = st.text_input("ユーザー名", placeholder="例: your_username")
    password = st.text_input("パスワード", type="password")
    warehouse = st.text_input("ウェアハウス", placeholder="例: your_warehouse")
    database = st.text_input("データベース", placeholder="例: your_database")
    schema = st.text_input("スキーマ", placeholder="例: your_schema")
    
    if st.button("接続テスト"):
        # ここに実際のSnowflake接続ロジックを実装
        st.success("接続テスト成功!")

# 右カラム: セグメント作成画面
with right_column:
    st.header("セグメント作成")
    
    # セグメント基本情報
    segment_name = st.text_input("セグメント名", placeholder="例: アクティブユーザー")
    
    # 条件設定エリア
    st.subheader("条件設定")
    
    # 行動条件
    st.markdown("**行動条件**")
    behavior_metric = st.selectbox(
        "指標選択",
        ["ウェブサイト訪問回数", "商品購入回数", "メール開封率"]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        operator = st.selectbox("条件", ["以上", "以下", "等しい"])
    with col2:
        threshold = st.number_input("値", min_value=0)
    
    # 期間設定
    st.markdown("**期間設定**")
    date_range = st.date_input("対象期間", [])
    
    # 属性条件
    st.markdown("**属性条件**")
    attributes = st.multiselect(
        "属性選択",
        ["年齢", "性別", "地域", "会員ランク"]
    )
    
    # セグメント作成ボタン
    if st.button("セグメント作成"):
        # ここに実際のセグメント作成ロジックを実装
        st.success("セグメントが作成されました!")
        
        # サンプルデータの表示
        sample_data = pd.DataFrame({
            'ユーザーID': range(1, 6),
            '年齢': [25, 30, 35, 40, 45],
            behavior_metric: [10, 5, 8, 12, 3]
        })
        st.dataframe(sample_data)
        
        # セグメントサイズの可視化
        fig = go.Figure(data=[go.Pie(labels=['セグメント対象', '非対象'], values=[30, 70])])
        fig.update_layout(title='セグメント構成比')
        st.plotly_chart(fig)

# 必要なライブラリをrequirements.txtに記載
# streamlit
# pandas
# plotly
