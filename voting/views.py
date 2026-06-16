from .models import Voter
from .models import Candidate, Vote, ElectionResult, Voter
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.http import JsonResponse
import json
from .models import Candidate

def chatbot(request):

    if request.method == "POST":

        data = json.loads(request.body)
        message = data.get("message", "").lower()

        if message in ["hi", "hello", "hey"]:
            reply = "Hello! Welcome to VoteSphere."

        elif "candidate" in message:
            count = Candidate.objects.count()
            reply = f"There are {count} candidates."

        elif "result" in message:
            reply = "Results will be announced by the administrator."

        elif "vote" in message:
            reply = "Select a candidate and click the Vote button."

        else:
            reply = "Please ask about candidates, voting, or results."

        return JsonResponse({"reply": reply})

    return JsonResponse({"reply": "Invalid request"})

    

@login_required
def home(request):

    candidates = Candidate.objects.all()

    voter = None

    if not request.user.is_superuser:
        try:
            voter = Voter.objects.get(user=request.user)

            print("USER =", voter.user.username)
            print("USN =", voter.usn)

        except Voter.DoesNotExist:
            print("NO VOTER FOUND")

    return render(
        request,
        'vote.html',
        {
            'candidates': candidates,
            'voter': voter,
        }
    )


@login_required
def vote(request, candidate_id):

    already_voted = Vote.objects.filter(
        voter=request.user
    ).exists()

    if already_voted:

        return render(
            request,
            "already_voted.html"
        )

    candidate = Candidate.objects.get(id=candidate_id)

    Vote.objects.create(
        voter=request.user,
        candidate=candidate
    )

    return render(
        request,
        "success.html"
    )


@login_required
def results(request):

    results = Candidate.objects.annotate(
        total_votes=Count('vote')
    )

    total_votes = Vote.objects.count()

    winner = results.order_by(
        '-total_votes'
    ).first()

    labels = []
    data = []

    for candidate in results:
        labels.append(candidate.name)
        data.append(candidate.total_votes)

    context = {
        'results': results,
        'winner': winner,
        'total_votes': total_votes,
        'total_voters': total_votes,
        'labels': labels,
        'data': data,
    }

    if request.user.is_superuser:

        return render(
            request,
            'results.html',
            context
        )

    status = ElectionResult.objects.first()

    if not status or not status.result_declared:

        return render(
            request,
            'result_locked.html'
        )

    return render(
        request,
        'results.html',
        context
    )


def custom_login(request):

    error = ""

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        usn = request.POST.get("usn", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Admin login
            if user.is_superuser:
                login(request, user)
                return redirect('/admin/')
            # Voter login
            try:
                voter = Voter.objects.get(user=user)

                if voter.usn != usn:
                    error = "Invalid USN"

                else:
                    login(request, user)
                    return redirect('/')

            except Voter.DoesNotExist:
                error = "Voter profile not found"

        else:
            error = "Wrong username or password"
    return render(
        request,
        'login.html',
        {'error': error}
    )