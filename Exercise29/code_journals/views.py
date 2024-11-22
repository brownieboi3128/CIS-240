from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import Topic
from . forms import TopicForm, EntryForm
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

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

def new_topic(request):
    """add a new topic."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = TopicForm()
    else:
        #POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('code_journals:topics'))
    
    context = {'form': form}
    return render(request, 'code_journals/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = EntryForm()
    else:
        #POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('code_journals:topic', args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'code_journals/new_entry.html', context)

def bar_chart(request):
    topics = Topic.objects.all()
    topics_entry_count = [(topic.text, topic.entry_set.count()) for topic in topics]
    df = pd.DataFrame(topics_entry_count, columns=['Topic', 'Entry Count'])
    # Instantiate a figure object
    fig = figure(x_range=df['Topic'], title='Entry Count by Topic', width=700, height=500)
    # Create a bar chart
    fig.vbar(source=df, x='Topic', top='Entry Count', width=0.9, color = "purple")
    html, div = components(fig)
    context = {'html': html, 'div': div}
    return render(request, 'code_journals/bar_chart.html', context)