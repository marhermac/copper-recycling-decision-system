# =====================================================
# Decision Lab
# Urban Mining Economics
# calculations.py
# =====================================================

def get_executive_metrics():

    """
    Executive indicators used throughout the application.

    In future versions these values will be calculated
    dynamically from the analytical model.
    """

    return {

        "best_asset": "Air Conditioner",

        "monthly_profit": 111750,

        "roi": 558.75,

        "confidence": "High",

        "payback": "2.1 months",

        "risk": "Medium",

        "investment": "Recommended"

    }


def executive_summary():

    return """
Among all evaluated assets, the Air Conditioner offers
the highest economic return due to its excellent balance
between copper recovery, processing costs and market value.

Current conditions indicate a strong investment opportunity
for small-scale urban mining operations.
"""


def key_findings():

    return [

        "Highest ROI among evaluated assets",

        "Highest estimated monthly profit",

        "Excellent operating margin",

        "Fast investment recovery",

        "High confidence level"

    ]