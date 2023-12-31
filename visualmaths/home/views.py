from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from students.forms import SignupForm
from students.forms import LoginForm, QuestionForm
from students.models import StudentUser, Question, MathsPoints, FurtherMathsPoints
from django.contrib.auth.hashers import check_password
from .decorators import user_login_required
import plotly.graph_objects as go

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

def recommend_maths(request):
    user = get_user(request)
    user_in_maths = MathsPoints.objects.get(username=user)
    fields = [f for f in MathsPoints._meta.get_fields() if f.name not in  ['id', 'username']]
    lowest_value = float('inf')
    
    for f in fields:
        value = getattr(user_in_maths, f.name)
        if value < lowest_value:
            lowest_value = value
            lowest_value_field = f.name
            return lowest_value_field
            
@user_login_required
def dash(request):
    if 'user_id' in request.session:
        user = get_user(request)
        append_to_furthermathspoints(request)
        append_to_mathspoints(request)
        mathstopic = recommend_maths(request)
        context = {
            'user':user,
            'mathstopic': mathstopic
            }
        return render(request, 'home/dash.html', context)
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

def determine_points(word):
    if word == "Easy":
        return 5
    elif word == "Medium":
        return 10
    elif word == "Hard":
        return 15

def question(request):
    subject =  request.GET.get('subject')
    topic =  request.GET.get('topic')
    difficulty =  request.GET.get('difficulty')
    student_questions = Question.objects.filter(subject=subject, topic=topic, difficulty=difficulty)
    #If a user submits their answers to their question
    if request.method == 'POST':
       
       #If the subject is maths or further maths
       if subject == "Maths":
            user = get_user(request)
            user_in_points = MathsPoints.objects.get(username=user)
            for q in student_questions:
                print(request.POST.get('dummy'))
                #Goes through topics for maths and increments based on topic variable
                #If the answer they have input is equal to the answer add to their points.
                if q.answer == request.POST.get(q.question):
                    if topic == "Quadratics":
                         user_in_points.quadratics += determine_points(difficulty)
                    elif topic == "Equations and Inequalities":
                         user_in_points.equations_and_inequalities += determine_points(difficulty)
                    elif topic == "Graphs and Transformations":
                         user_in_points.graphs_and_transformations += determine_points(difficulty)
                    elif topic == "Straight Line Graphs":
                         user_in_points.straight_line_graphs += determine_points(difficulty)
                    elif topic == "Circles":
                         user_in_points.circles += determine_points(difficulty)
                    elif topic == "Trigonometry":
                         user_in_points.trigonometry += determine_points(difficulty)
                    elif topic == "Differentiation":
                         user_in_points.differentiation += determine_points(difficulty)
                    elif topic == "Integration":
                        user_in_points.integration += determine_points(difficulty)
                    elif topic == "2D Vectors":
                        user_in_points.two_d_vectors += determine_points(difficulty)
                    user_in_points.save()

                    print(request.POST.get(q.question))
                    good_message = "Correct Answer!!"
                    context = {
                    'good': good_message,
                    'student_questions': student_questions,
                    }
                    return render(request, 'home/question.html', context)
                else:
                    bad_message = "Incorrect Answer."
                    context = {
                    'student_questions': student_questions,
                    'bad': bad_message,
                }
                    return render(request, 'home/question.html', context)
       else:
           user = get_user(request)
           user_in_points = FurtherMathsPoints.objects.get(username=user)
           for q in student_questions:
                
                if q.answer == request.POST.get(q.question):
                    if topic == "Argand Diagrams":
                         user_in_points.argand_diagrams += determine_points(difficulty)
                    elif topic == "Volumes of Revolution":
                         user_in_points.volumes_of_revolution += determine_points(difficulty)
                    elif topic == "Methods In Calculus":
                         user_in_points.methods_in_calculus += determine_points(difficulty)
                    elif topic == "Straight Line Graphs":
                         user_in_points.straight_line_graphs += determine_points(difficulty)
                    elif topic == "Matrices":
                         user_in_points.matrices += determine_points(difficulty)
                    elif topic == "Polar Coordinates":
                         user_in_points.polar_coordinates += determine_points(difficulty)
                    elif topic == "Hyperbolic Functions":
                         user_in_points.hyperbolic_functions += determine_points(difficulty)
                    elif topic == "Differentiation":
                         user_in_points.differentiation += determine_points(difficulty)
                    elif topic == "Integration":
                        user_in_points.integration += determine_points(difficulty)
                    elif topic == "3D Vectors":
                        user_in_points.three_d_vectors += determine_points(difficulty)
                    user_in_points.save()
                    good_message = "Correct Answer!!"
                    context = {
                    'good': good_message,
                    'student_questions': student_questions,
                    }
                    return render(request, 'home/question.html', context)
                else:
                    bad_message = "Incorrect Answer."
                    context = {
                    'student_questions': student_questions,
                    'bad': bad_message,
                }
                    return render(request, 'home/question.html', context)
           
    context = {
        'student_questions': student_questions,
    }
    return render(request, 'home/question.html', context)

def weeklyAssessments(request):
    user = get_user(request)
    user_in_maths = MathsPoints.objects.get(username=user)
    fig = go.Figure(data=go.Bar(x=['quadratics', 'circles'], y=[user_in_maths.quadratics, user_in_maths.circles]))
    chart = fig.to_html(full_html=False, default_height=500, default_width=700)
    context = {
        'chart': chart,
    }
    return render(request, 'home/assessment.html', context)
    