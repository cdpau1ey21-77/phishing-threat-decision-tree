import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import classification_report, confusion_matrix


DATA_PATH = "data/sample_emails.csv"
MODEL_PATH = "phishing_decision_tree.pkl"


FEATURE_COLUMNS = [
    "sender_domain_age_days",
    "sender_domain_matches_display_name",
    "has_urgent_language",
    "num_links_in_body",
    "link_domain_matches_sender_domain",
    "has_attachment",
    "attachment_is_executable",
    "spf_dkim_pass",
    "reply_to_differs_from_sender",
    "impersonates_known_brand",
]


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURE_COLUMNS]
    y = df["label"]

    X = X.replace({True: 1, False: 0})

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    model = DecisionTreeClassifier(
        max_depth=5,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nDecision Tree Rules:")
    print(export_text(model, feature_names=FEATURE_COLUMNS))

    joblib.dump(model, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
