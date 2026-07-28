"""Training script for MarketLens — Marketing Mix and Attribution Analytics Platform (MMMAAA)."""
import joblib, pandas as pd
FEATURES = ['media_spend_and_impression_data_by_channel_and_campaign', 'promotional_calendar_and_pricing_data', 'competitor_spend', 'weather', 'macroeconomic_indicators', 'category_level_trends']
TARGET = 'Weekly_sales_data_by_brand_and_geography'

def main(path="data.csv"):
    df = pd.read_csv(path)
    X = df[FEATURES].fillna(0).values
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score
    y = df[TARGET].values
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=120, random_state=42)
    model.fit(Xtr, ytr)
    try:
        score = roc_auc_score(yte, model.predict_proba(Xte)[:, 1])
    except Exception:
        score = model.score(Xte, yte)
    print("roc_auc/score:", score)
    joblib.dump(model, "model.joblib")
    print("saved model.joblib")

if __name__ == "__main__":
    main()
