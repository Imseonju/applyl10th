from django.db.models.manager import EmptyManager
from django.shortcuts import redirect, render, get_object_or_404
from.models import Apply
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home2(request):
    allforms = Apply.objects.all()
    count = allforms.count()
    return render(request, 'home2.html', {'aa':allforms, 'count':count})

def detail(request, id):
    oneform = get_object_or_404(Apply, pk = id)
    return render(request, 'detail.html', {'b':oneform})

def new(request):
    return render(request, 'new.html')

def create(request):
    if Apply.objects.filter(snum = request.POST['sn']).exists():
        eapply = get_object_or_404(Apply, snum = request.POST['sn'])
        messages.info(request, '한 계정당 하나의 지원서만 작성 가능합니다!')
        return redirect('urldetail', eapply.id)
    nform = Apply()
    nform.motive = request.POST['m']
    nform.service = request.POST['s']
    nform.pac = request.POST['p']
    nform.conflict = request.POST['c']
    nform.aspire = request.POST['a']
    nform.image = request.FILES.get('image')
    nform.s_time = timezone.now()
    nform.name = request.POST['n']
    nform.dept = request.POST['d']
    nform.snum = request.POST['sn']
    nform.save()
    return redirect('urldetail', nform.id)

def edit(request, id):
    eform = Apply.objects.get(id = id)
    return render(request, 'edit.html', {'e':eform})

def update(request, id):
    uform = Apply.objects.get(id = id)
    uform.motive = request.POST['um']
    uform.service = request.POST['us']
    uform.pac = request.POST['up']
    uform.conflict = request.POST['uc']
    uform.aspire = request.POST['ua']
    uform.image = request.FILES.get('uimage')
    uform.s_time = timezone.now()
    uform.name = request.POST['un']
    uform.dept = request.POST['ud']
    uform.snum = request.POST['usn']
    uform.save()
    return redirect('urldetail', uform.id)

def delete(request, id):
    dform = Apply.objects.get(id = id)
    dform.delete()
    return redirect('urlhome2')