from django.shortcuts import render

from . models import Topic

# Create your views here.
def index(request):
    """The home page for code_journals."""
    return render(request, 'code_journals/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics, 'other_topics': ['other_topics']}
    return render(request, 'code_journals/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'code_journals/topic.html', context)