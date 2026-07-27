import re
from textblob import TextBlob

def analyze_seo(content, keyword):

    words = re.findall(r'\w+', content.lower())
    total_words = len(words)

    keyword_count = content.lower().count(keyword.lower())

    keyword_density = (keyword_count / total_words) * 100 if total_words > 0 else 0

    polarity = TextBlob(content).sentiment.polarity

    score = 0

    if total_words >= 300:
        score += 30
    elif total_words >= 150:
        score += 20
    else:
        score += 10

    if 1 <= keyword_density <= 3:
        score += 40
    else:
        score += 20

    if polarity >= 0:
        score += 30
    else:
        score += 20

    suggestions = []

    if total_words < 300:
        suggestions.append("Increase content length to at least 300 words.")

    if keyword_density < 1:
        suggestions.append("Use the keyword more frequently.")

    if keyword_density > 3:
        suggestions.append("Reduce keyword stuffing.")

    if polarity < 0:
        suggestions.append("Try to use a more positive tone.")

    return {
        "Total Words": total_words,
        "Keyword Count": keyword_count,
        "Keyword Density (%)": round(keyword_density, 2),
        "SEO Score": score,
        "Suggestions": suggestions
    }