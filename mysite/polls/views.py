from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F


# polls index
def index(request):
    # 展示数据库里以发布日期排序的最近的5个问题，并以“”“","进行分隔
    last_question_list = Question.objects.order_by('pub_date')[:5]
    return render(request, "polls/index.html", {'last_question_list': last_question_list})

# question_detail
def detail(request, question_id):
    # 显示指定投票的问题标题
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist.")
    return render(request, 'polls/detail.html', {'question':question})

# question_results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})


# question_vote
def vote(request, question_id):
    # 投票处理器
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "Your don't select the choice. "
                      })
    else:
        # selected_choice.votes += 1
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))







