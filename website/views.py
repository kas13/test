from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
#from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from .models import Post, UserCreation, SubjectList
from .forms import PostForm, UserCreationForm, SubjectCreationForm, CreateQuestionForm
from .DBhelper import *


database_connection = DatabaseConnection()
# Create your views here.

def base(request):
    subjects_list = SubjectList.objects.all()
    return render(request, 'website/base.html', {'subjects_list': subjects_list})

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'website/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'website/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'website/post_edit.html', {'form': form}) 

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'website/post_edit.html', {'form': form})


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(name, email, password)
        user.save()
        return redirect('/')
    else:
        print("else")
        data, errors = {}, {}

    return render (request,"registration/register.html", {'form': form})

def new_test(request):
    if request.method == 'POST':
        form = SubjectCreationForm(request.POST)
        if form.is_valid():
            name_subject = request.POST['name']
            result = database_connection.create_table_subject(name_subject)
            if result is True:
                subject = form.save()
                subject.save()
                print("SAVE", name_subject)
            return redirect('/')
    else:
        print("else")
        form = SubjectCreationForm()
    subjects_list = SubjectList.objects.all()
    #     subjects_list = []
    # for subject in SubjectList.objects.all():
    #     subjects_list.append(subject.name)
    return render (request,"website/new_test.html", {'subjects_list': subjects_list, 'form': form})


def create_test(request, name):
    table = database_connection.show_questions(name)
    print(table)
    if request.method == 'POST':
        print(request.POST)
        question = request.POST['question']
        variants = request.POST['variants']
        answer = request.POST['answer']
        database_connection.save_question(name, question, variants, answer)
    else:
        pass
    form = CreateQuestionForm()
    return render (request,"website/create_test.html", {'form': form, 'table': table})


def new_questions(request, name):
    table = database_connection.show_questions(name)
    print(table)
    if request.method == 'POST':
        print(request.POST)
        question = request.POST['question']
        variants = request.POST['variants']
        answer = request.POST['answer']
        database_connection.save_question(name, question, variants, answer)
    else:
        pass
    form = CreateQuestionForm()
    return render (request,"website/new_questions.html", {'form': form, 'table': table})



def add_questions(request):
    subjects_list = SubjectList.objects.all()
    return render (request,"website/add_questions.html", {'subjects_list': subjects_list})

    # table = database_connection.show_questions(name)
    # print(table)
    # if request.method == 'POST':
    #     print(request.POST)
    #     question = request.POST['question']
    #     variants = request.POST['variants']
    #     answer = request.POST['answer']
    #     database_connection.save_question(name, question, variants, answer)
    # else:
    #     pass
    # form = CreateQuestionForm()
    # return render (request,"website/create_test.html", {'form': form, 'table': table})

def start_test(request, name, pk):
    tests = database_connection.get_tests(name)
    num_of_question = int(pk)
    question = tests[num_of_question][1]
    variants = tests[num_of_question][2]
    answer = tests[num_of_question][3]
    print(variants)

    return render (request,"website/start_test.html", {'num_of_question': num_of_question + 1, 'question': question,
                                                       'variants': variants, 'answer': answer})
