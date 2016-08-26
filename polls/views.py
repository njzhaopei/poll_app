from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponseRedict
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
	template_name = "polls/index.html"
	context_object_name = "latest_question_list"
	def get_queryset(self):
		"""return the last five published questions"""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = "polls/details.html"

class ResultsView(generic.DetailView):
	model = Question
	template_name = "polls/results.html"
	def vote(request, question_id):
		#same as above , no changes needed

