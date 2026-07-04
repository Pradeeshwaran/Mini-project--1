def cal_score(data):
    score = 0

    if 6 <= data["sleep"] <= 8:
        score += 20
    if 2 <= data["water"] <= 4:
        score += 20
    if data["exercise"] >= 30:
        score += 20
    if 60 <= data["heart_rate"] <= 100:
        score += 20
    if 18.5 <= data["bmi"] <= 24.9:
        score += 20

    return score


def risk_level(score):
    if score >= 80:
        return "Low Risk"
    elif score >= 50:
        return "Medium Risk"
    else:
        return "High Risk"


def suggestions(data):
    suggestions = []

    if data["sleep"] < 6:
        suggestions.append("Improve sleep")
    if data["water"] < 2:
        suggestions.append("Drink more water")
    if data["exercise"] < 30:
        suggestions.append("Do regular exercise")
    if not (60 <= data["heart_rate"] <= 100):
        suggestions.append("Check heart rate")
    if not (18.5 <= data["bmi"] <= 24.9):
        suggestions.append("Maintain healthy BMI")

    return ", ".join(suggestions) if suggestions else "All Good"
