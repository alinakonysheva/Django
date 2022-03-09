from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.db.models import Q, Count
from django.contrib import messages
from mycv.models import ResumeItem, Skill
from mycv.forms import ResumeItemForm, SkillForm


# Create your views here.


def do_home(request):
    resume_items = ResumeItem.objects.all()
    return render(request, 'mycv/home.html', context={'resume_items': resume_items})


def do_search(request):
    if request.method == 'POST':
        try:
            search_text = request.POST.get('do_search', '')
            if search_text != '':
                pass
        except:
            pass
    return render(request, 'mycv/search_results.html', context={'test': None})


def do_experience(request, experience_id):
    item = get_object_or_404(ResumeItem, pk=experience_id)
    if request.method == 'POST':
        form = ResumeItemForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Aangepast')
            return redirect(reverse('mycv:do_experience', args={experience_id: experience_id}))
    else:
        item = get_object_or_404(ResumeItem, pk=experience_id)
        ctx = {"form": ResumeItemForm(instance=item), 'item': item}
        return render(request, 'mycv/experience.html', context=ctx)


def do_experience_add(request):
    if request.method == 'POST':
        form = ResumeItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '{} toegevoegd aan de lijst'.format(form.instance))
            return redirect(reverse('mycv:do_home'))
    else:
        ctx = {'form': ResumeItemForm()}
        return render(request, "mycv/experience.html", ctx)


def do_skills(request):
    skills = Skill.objects.all()
    return render(request, 'mycv/skill_list.html', context={'skills': skills})


def do_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    if request.method == 'POST':
        form = SkillForm(request.POST or None, item=skill)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Aangepast')
            return redirect(reverse('mycv:do_skill', args={skill_id: skill_id}))
    else:
        skill = get_object_or_404(Skill, pk=skill_id)
        ctx = {"form": SkillForm(instance=skill), 'skill': skill}
        return render(request, 'mycv/skill.html', context=ctx)


def do_skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '{} toegevoegd aan de lijst'.format(form.instance))
            return redirect(reverse('mycv:do_skills'))
    else:
        ctx = {'form': SkillForm()}
        return render(request, "mycv/skill.html", ctx)


def do_most_used(request):
    items = Skill.objects.annotate(skill_count=Count('resume_items')).order_by('-skill_count')[:10]

    return render(request, 'mycv/most_used.html', context={'items': items})


