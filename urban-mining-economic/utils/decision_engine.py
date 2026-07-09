# ==========================================================
# Decision Lab
# Urban Mining Economics
#
# Decision Engine v1.0
# ==========================================================

ASSETS = [

    {
        "name": "Air Conditioner",
        "roi": 558.75,
        "profit": 111750,
        "risk": "Medium"
    },

    {
        "name": "Refrigerator",
        "roi": 220.40,
        "profit": 45780,
        "risk": "High"
    },

    {
        "name": "Washing Machine",
        "roi": 310.10,
        "profit": 58940,
        "risk": "Medium"
    },

    {
        "name": "Microwave",
        "roi": 485.20,
        "profit": 82100,
        "risk": "Low"
    },

    {
        "name": "Electric Motor",
        "roi": 375.80,
        "profit": 64320,
        "risk": "Medium"
    }

]


def best_asset():

    return max(
        ASSETS,
        key=lambda asset: asset["roi"]
    )


def ranking():

    return sorted(
        ASSETS,
        key=lambda asset: asset["roi"],
        reverse=True
    )
# ==========================================================
# DECISION RECOMMENDATION
# ==========================================================

def recommendation():

    winner = best_asset()

    if winner["roi"] >= 500:

        stars = "★★★★★"

        level = "Excellent Investment"

        color = "🟢"

    elif winner["roi"] >= 350:

        stars = "★★★★☆"

        level = "Very Good Investment"

        color = "🟢"

    elif winner["roi"] >= 250:

        stars = "★★★☆☆"

        level = "Moderate Investment"

        color = "🟡"

    else:

        stars = "★★☆☆☆"

        level = "High Risk"

        color = "🔴"

    return {

        "asset": winner["name"],

        "roi": winner["roi"],

        "profit": winner["profit"],

        "risk": winner["risk"],

        "stars": stars,

        "level": level,

        "color": color

    }