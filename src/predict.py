import joblib
import pandas as pd


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


def classify_email(email_features):
    model = joblib.load(MODEL_PATH)

    input_df = pd.DataFrame([email_features])
    input_df = input_df[FEATURE_COLUMNS]
    input_df = input_df.replace({True: 1, False: 0})

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    return prediction, probabilities


if __name__ == "__main__":
    test_email = {
        "sender_domain_age_days": 7,
        "sender_domain_matches_display_name": False,
        "has_urgent_language": True,
        "num_links_in_body": 4,
        "link_domain_matches_sender_domain": False,
        "has_attachment": True,
        "attachment_is_executable": True,
        "spf_dkim_pass": False,
        "reply_to_differs_from_sender": True,
        "impersonates_known_brand": True,
    }

    label, probabilities = classify_email(test_email)

    print("Prediction:", label)
    print("Class probabilities:", probabilities)
