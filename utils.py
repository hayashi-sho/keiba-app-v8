import pandas as pd

def load_data(url):
    try:
        # 仮のダミーデータとしてCSVを作成（本来はスクレイピングやAPI取得処理）
        df = pd.DataFrame({
            "馬名": ["サンプルホースA", "サンプルホースB"],
            "脚質": ["先行", "差し"],
            "騎手": ["騎手A", "騎手B"],
            "人気": [1, 2],
            "タイム指数": [82, 78]
        })
        return df
    except Exception as e:
        return None

def calculate_ai_index(row):
    base = 50
    if row["人気"] == 1:
        base += 10
    if row["脚質"] == "先行":
        base += 5
    return base + row["タイム指数"] * 0.2
