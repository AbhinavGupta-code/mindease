from django.shortcuts import render, redirect
from .forms import MoodEntryForm
from .models import MoodEntry
from textblob import TextBlob
from django.utils import timezone
from datetime import timedelta



def daily_checkin(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)

            # AI sentiment analysis
            analysis = TextBlob(entry.reflection)
            polarity = analysis.sentiment.polarity
            entry.sentiment_score = polarity

            if polarity > 0.1:
                entry.sentiment_label = "Positive"
            elif polarity < -0.1:
                entry.sentiment_label = "Negative"
            else:
                entry.sentiment_label = "Neutral"

            entry.save()
            return redirect('success')
    else:
        form = MoodEntryForm()

    return render(request, 'checkin/checkin.html', {'form': form})


def success(request):
    return render(request, 'checkin/success.html')

def dashboard(request):
    entries = MoodEntry.objects.order_by('-created_at')
    total_entries = entries.count()
    latest_entry = entries.first()

    
    last_week = timezone.now() - timedelta(days=7)
    weekly_entries = MoodEntry.objects.filter(created_at__gte=last_week)

    positive = weekly_entries.filter(sentiment_label="Positive").count()
    neutral = weekly_entries.filter(sentiment_label="Neutral").count()
    negative = weekly_entries.filter(sentiment_label="Negative").count()

    
    suggestion = "Keep checking in daily to understand your mood patterns."

    if negative > positive and negative > neutral:
        suggestion = (
            "You've had more negative days recently. "
            "Consider taking short breaks, talking to someone you trust, "
            "and focusing on rest and self-care."
        )
    elif positive > negative and positive > neutral:
        suggestion = (
            "You've been feeling positive lately. "
            "Keep maintaining the habits that are working well for you!"
        )
    elif neutral > 0:
        suggestion = (
            "Your mood seems mixed or neutral. "
            "Try journaling or reflecting on what influences your days."
        )

    return render(request, 'checkin/dashboard.html', {
        'entries': entries,
        'total_entries': total_entries,
        'latest_entry': latest_entry,
        'positive': positive,
        'neutral': neutral,
        'negative': negative,
        'suggestion': suggestion,
    })
