"""
Project: Lumina Beauty Brand Lift Measurement Study

Purpose:
Programmatically generate a realistic synthetic survey dataset
to simulate consumer responses to a digital marketing campaign.

The simulated dataset models:
- Campaign exposure
- Ad frequency
- Creative type
- Demographics
- Brand lift outcomes

The resulting dataset is exported as a CSV and used for SQL
analysis and Tableau dashboard development.

Tools:
- Python
- Pandas
- Random
"""

# ==========================================================
# Import Libraries
# ==========================================================

import os
import pandas as pd
import random


# ==========================================================
# Project Configuration
# ==========================================================

print("Welcome to the Lumina Beauty Brand Lift Study!")

respondents = 5000
random.seed(42)

print(f"Generating {respondents} survey responses...")


# ==========================================================
# Survey Categories
# ==========================================================

devices = ["Mobile", "CTV", "Social Video"]
age_groups = ["18-24", "25-34", "35-44", "45-54", "55+"]
genders = ["Female", "Male", "Non-binary"]
regions = ["Northeast", "Midwest", "South", "West"]
exposure_groups = ["Exposed", "Control"]
frequency_buckets = ["1 exposure", "2-3 exposures", "4-5 exposures", "6+ exposures"]
creative_types = ["Product Demo", "Lifestyle Video", "Influencer Testimonial"]


# ==========================================================
# Generate Synthetic Survey Responses
# ==========================================================

survey_data = []

for respondent_id in range(1, respondents + 1):
    device = random.choice(devices)
    age = random.choice(age_groups)
    gender = random.choice(genders)
    region = random.choice(regions)
    exposure = random.choice(exposure_groups)

    if exposure == "Exposed":
        frequency = random.choices(
            frequency_buckets,
            weights=[35, 30, 20, 15]
        )[0]
        creative = random.choice(creative_types)
    else:
        frequency = "No Exposure"
        creative = "No Creative"

    # ------------------------------------------------------
    # Simulate Ad Recall
    # ------------------------------------------------------

    if exposure == "Control":
        recall_probability = 0.38
    else:
        if frequency == "1 exposure":
            recall_probability = 0.55
        elif frequency == "2-3 exposures":
            recall_probability = 0.68
        elif frequency == "4-5 exposures":
            recall_probability = 0.78
        else:
            recall_probability = 0.86

        if device == "Social Video":
            recall_probability += 0.05
        elif device == "CTV":
            recall_probability += 0.03

        if creative == "Influencer Testimonial":
            recall_probability += 0.04
        elif creative == "Product Demo":
            recall_probability += 0.02

        if age == "18-24":
            recall_probability += 0.04
        elif age == "25-34":
            recall_probability += 0.02
        elif age == "45-54":
            recall_probability -= 0.01
        elif age == "55+":
            recall_probability -= 0.03

        if gender == "Female":
            recall_probability += 0.02
        elif gender == "Male":
            recall_probability -= 0.01

        if region == "West":
            recall_probability += 0.03
        elif region == "Northeast":
            recall_probability += 0.01
        elif region == "Midwest":
            recall_probability -= 0.02

        recall_probability = max(0.05, min(recall_probability, 0.95))

    ad_recall = "Yes" if random.random() < recall_probability else "No"

    # ------------------------------------------------------
    # Simulate Brand Awareness
    # ------------------------------------------------------

    if exposure == "Control":
        awareness_probability = 0.45
    else:
        awareness_probability = 0.70

        if age in ["18-24", "25-34"]:
            awareness_probability += 0.03

        if region == "West":
            awareness_probability += 0.02
        elif region == "Midwest":
            awareness_probability -= 0.02

        awareness_probability = max(0.05, min(awareness_probability, 0.95))

    brand_awareness = "Yes" if random.random() < awareness_probability else "No"

    # ------------------------------------------------------
    # Simulate Brand Favorability
    # ------------------------------------------------------

    if exposure == "Control":
        favorability_probability = 0.42
    else:
        favorability_probability = 0.61

        if gender == "Female":
            favorability_probability += 0.03

        if creative == "Influencer Testimonial":
            favorability_probability += 0.03
        elif creative == "Product Demo":
            favorability_probability += 0.01

        favorability_probability = max(0.05, min(favorability_probability, 0.95))

    brand_favorability = (
        "Favorable"
        if random.random() < favorability_probability
        else "Neutral/Unfavorable"
    )

    # ------------------------------------------------------
    # Simulate Purchase Intent
    # ------------------------------------------------------

    if exposure == "Control":
        purchase_probability = 0.32
    else:
        purchase_probability = 0.48

        if age == "25-34":
            purchase_probability += 0.04
        elif age == "18-24":
            purchase_probability += 0.02
        elif age == "55+":
            purchase_probability -= 0.03

        if brand_favorability == "Favorable":
            purchase_probability += 0.08

        purchase_probability = max(0.05, min(purchase_probability, 0.95))

    purchase_intent = "Likely" if random.random() < purchase_probability else "Not Likely"

    respondent = {
        "respondent_id": respondent_id,
        "device": device,
        "age_group": age,
        "gender": gender,
        "region": region,
        "exposed_group": exposure,
        "frequency_bucket": frequency,
        "creative_type": creative,
        "ad_recall": ad_recall,
        "brand_awareness": brand_awareness,
        "brand_favorability": brand_favorability,
        "purchase_intent": purchase_intent
    }

    survey_data.append(respondent)


# ==========================================================
# Create DataFrame
# ==========================================================

survey_df = pd.DataFrame(survey_data)

print("\nData Preview:")
print(survey_df.head())


# ==========================================================
# Export Dataset
# ==========================================================

os.makedirs("data", exist_ok=True)

survey_df.to_csv(
    "data/survey_responses.csv",
    index=False
)

print("\nCSV file created: data/survey_responses.csv")


# ==========================================================
# Validation Checks
# ==========================================================

print("\nExposure Group Counts:")
print(survey_df["exposed_group"].value_counts())

print("\nAd Recall by Exposure Group:")
print(pd.crosstab(survey_df["exposed_group"], survey_df["ad_recall"], normalize="index") * 100)

print("\nAd Recall by Age Group:")
print(pd.crosstab(survey_df["age_group"], survey_df["ad_recall"], normalize="index") * 100)

print("\nAd Recall by Gender:")
print(pd.crosstab(survey_df["gender"], survey_df["ad_recall"], normalize="index") * 100)

print("\nAd Recall by Region:")
print(pd.crosstab(survey_df["region"], survey_df["ad_recall"], normalize="index") * 100)

print("\nBrand Awareness by Exposure Group:")
print(pd.crosstab(survey_df["exposed_group"], survey_df["brand_awareness"], normalize="index") * 100)

print("\nPurchase Intent by Exposure Group:")
print(pd.crosstab(survey_df["exposed_group"], survey_df["purchase_intent"], normalize="index") * 100)
