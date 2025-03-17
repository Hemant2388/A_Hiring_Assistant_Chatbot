import os
import pandas as pd
from datetime import datetime

def mask_email(email):
    return email[:2] + "*****" + email[-2:]

def save_candidate_data(candidate_info, file_path="candidate_data.csv"):
    candidate_info["Email"] = mask_email(candidate_info["Email"])
    candidate_info["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print(f"⚠️ CSV read error: {e}")
            df = pd.DataFrame(columns=candidate_info.keys())
    else:
        df = pd.DataFrame(columns=candidate_info.keys())

    df = pd.concat([df, pd.DataFrame([candidate_info])], ignore_index=True)
    df.to_csv(file_path, index=False)
