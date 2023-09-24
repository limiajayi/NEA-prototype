from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from students.forms import SignupForm
from students.forms import LoginForm, QuestionForm
from students.models import StudentUser, Question, MathsPoints, FurtherMathsPoints
from django.contrib.auth.hashers import check_password
from .decorators import user_login_required

# Create your views here.

def homepage(request):
    template = loader.get_template('home/homepage.html')
    return HttpResponse(template.render())


def signup(request):
    form = SignupForm()
    success = None
    if request.method =='POST':
        if StudentUser.objects.filter(username=request.POST['username']):
            error = "This username is already taken"
            return render(request, 'home/signup.html', {'form': form, 'error': error})
        form = SignupForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "Student Account created successfully!"
        return render(request, 'home/signup.html', {'form': form, 'success': success})
    return render(request, 'home/signup.html', {'form': form})
    

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        passsword = request.POST['password']
        if StudentUser.objects.filter(username=username).exists():
            user = StudentUser.objects.get(username=username)
            valid = check_password(passsword, user.password)
            if valid:
              request.session['user_id'] = user.id
              return redirect('/home/dash/')
            else:
                password_error = "Incorrect Password"
                context = {'form': form, 
                           'password_error': password_error}
                return render(request, 'home/login.html', context)
        else:
            error = "Incorrect Username"
            context = {'form': form, 
                       'error': error}
            return render(request, 'home/login.html', context)
    return render(request, 'home/login.html', {'form': form})


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/home/')

def graph(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'home/graph.html', {'user':user})
    else:
        return redirect('/home/signup/')

def get_user(request):
    return StudentUser.objects.get(id=request.session['user_id'])

def append_to_mathspoints(request):
    user = get_user(request)
    if MathsPoints.objects.filter(username=user).exists():
        return None
    elif user.maths == True:
        new_user = MathsPoints(username=user)
        new_user.save()
    
def append_to_furthermathspoints(request):
    user = get_user(request)
    if FurtherMathsPoints.objects.filter(username=user).exists():
        return None
    elif user.further_maths == True:
        new_user = FurtherMathsPoints(username=user)
        new_user.save()
            
@user_login_required
def dash(request):
    if 'user_id' in request.session:
        user = get_user(request)
        append_to_furthermathspoints(request)
        append_to_mathspoints(request)
        return render(request, 'home/dash.html', {'user':user})
    else:
        return redirect('/home/signup/')

def subject(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'home/subject.html', {'user':user})
    else:
        return redirect('/home/signup/')
    
def qform(request):
    form = QuestionForm()
    if request.method == 'POST':
        subject = request.POST['subject']
        topic = request.POST['topic']
        difficulty = request.POST['difficulty']
        return redirect('/home/question/?subject=' + subject + '&topic=' + topic + '&difficulty=' + difficulty)
    
    context = {
        'form': form
    }
    return render(request, 'home/qform.html', context)

def question(request):
    subject =  request.GET.get('subject')
    topic =  request.GET.get('topic')
    difficulty =  request.GET.get('difficulty')
    student_questions = Question.objects.filter(subject=subject, topic=topic, difficulty=difficulty)
    if request.method == 'POST':
        for q in student_questions:
            print(request.POST.get(q.question))
            if q.answer == request.POST.get(q.question):
                markscheme = q.mark_scheme.url
                good_message = "Correct Answer!!"
                context = {
                    'good': good_message,
                    'markscheme': markscheme,
                    'student_questions': student_questions,
                }
                return render(request, 'home/question.html', context)
            else:
                bad_message = "Incorrect Answer."
                markscheme = q.mark_scheme.url
                context = {
                    'student_questions': student_questions,
                    'bad': bad_message,
                    'markscheme': markscheme,
                }
                return render(request, 'home/question.html', context)
    context = {
        'student_questions': student_questions
    }
    return render(request, 'home/question.html', context)