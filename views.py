import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Prefecture, Photo

def map_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if 'toggle_home' in data:
                pref_name = data['toggle_home']
                pref = Prefecture.objects.get(name=pref_name)
                pref.is_home = not pref.is_home
                pref.save()
                return JsonResponse({'status': 'ok'})
        except:
            pass

    prefectures = Prefecture.objects.all()
    pref_list = []
    for p in prefectures:
        pref_list.append({
            'name': p.name,
            'visit_date': p.visit_date,
            'has_photos': p.photos.exists(),
            'is_home': p.is_home
        })
    
    context = {'pref_json': json.dumps(pref_list)}
    return render(request, 'triplog/map.html', context)

def detail_view(request, pref_name):
    pref = get_object_or_404(Prefecture, name=pref_name)
    photos = pref.photos.all()

    if request.method == "POST":
        if 'delete_photo_id' in request.POST:
            photo_id = request.POST.get('delete_photo_id')
            Photo.objects.filter(id=photo_id, prefecture=pref).delete()
            return redirect('detail', pref_name=pref.name)

        if request.FILES.getlist('images'):
            for img in request.FILES.getlist('images'):
                Photo.objects.create(prefecture=pref, image=img)
            return redirect('detail', pref_name=pref.name)
        
        try:
            data = json.loads(request.body)
            if 'visit_date' in data:
                pref.visit_date = data['visit_date']
                pref.save()
                return JsonResponse({'status': 'ok'})
        except:
            pass

    # データベースのID（1〜47）を使って色を計算（日本語リスト不要に！）
    try:
        idx = pref.id - 1
        h = (idx / 47.0) * 360
        bg_color = f"hsl({h}, 85%, 93%)"
        main_color = f"hsl({h}, 85%, 50%)"
    except:
        bg_color = "#f4f7f6"
        main_color = "#3498db"

    return render(request, 'triplog/detail.html', {
        'pref': pref, 
        'photos': photos,
        'bg_color': bg_color,
        'main_color': main_color
    })