from django.shortcuts import render
from django.http import HttpResponse

from app.models import *

# Create your views here.


def insert_topic(request):
    
    if request.method =='POST':
        topic = request.POST['topic']
        Tupleoftopicobject = Topic.objects.get_or_create(topic_name = topic)
        
        if Tupleoftopicobject[1]:
            return HttpResponse('Object is created')
        else:
            return HttpResponse('object is already present')
    
    return render(request ,'insert_topic.html')


def insert_webpage(request):   
    querysetoflistoftopicobject = Topic.objects.all()
    d = {'querysetoflistoftopicobject': querysetoflistoftopicobject}

    if request.method == 'POST':
        tn = request.POST['topic_name']
        to = Topic.objects.get(topic_name=tn)
        na = request.POST['name']
        ur = request.POST['url']

        TWO = Webpage.objects.get_or_create(topic=to, name=na, url=ur)

        if TWO[1]:
            return HttpResponse('Object is created')
        else:
            return HttpResponse('Object is already present')

    return render(request, 'insert_webpage.html', d)


def insert_accessrecord(request):
    querysetoflistofwebpageobject = Webpage.objects.all()
    d = {'querysetoflistofwebpageobject': querysetoflistofwebpageobject}

    if request.method == 'POST':
        n = request.POST['name']
        na = Webpage.objects.get(name=n)
        at = request.POST['author']
        da = request.POST['date']

        TWO = AccessRecord.objects.get_or_create(
            name=na,
            author=at,
            date=da
        )

        if TWO[1]:
            return HttpResponse('Object is created')
        else:
            return HttpResponse('Object is already present')

    return render(request, 'insert_accessrecord.html', d)











# from django.shortcuts import render

# from django.http import HttpResponse

# from app.models import *

# Create your views here.

# def insert_Topic(request):
#     tn = input('Enter topic name:')
#     TTO= Topic.objects.get_or_create(topic_name = tn)
#     if TTO[1]:
#         return HttpResponse('New topic is created')
#     else:
#         return HttpResponse('Topic is already present')

# def insert_webpage(request):
#     print('Existing topic')
#     for to in Topic.objects.all():
#         print(to.topic_name)
#     tn = input('enter the name of topic:')
#     LTO = Topic.objects.filter(topic_name = tn)
#     if LTO:
#         STO = LTO[0]
#         na = input('enter the name:')
#         ur = input('enter the url:')
#         TWO = Webpage.objects.get_or_create(topic =STO, name=na, url =ur)
#         if TWO[1]:
#             LOW = Webpage.objects.all()
#             print('Existing Webpages')
#             d = {'webpages': LOW}
#             return render(request, 'Display_webpage.HTML', d)
#         else:     
#             return HttpResponse('Webpage is already present')
#     else:
#         return HttpResponse('Topic is not present')
    
# def insert_Accessrecord(request):
#     print('Existing Web pages')
#     for wp in Webpage.objects.all():
#         print(wp.name)
#     n = input('Enter the name')
#     LWO = Webpage.objects.filter(name = n)
#     if LWO:
#         SWO =LWO[0]    
#         at = input('Enter the author name :')
#         da = input('Enter the date:')
#         TWO = AccessRecord.objects.get_or_create(name = SWO,author = at ,date = da,)
#         if TWO[1]:
#             LOA = AccessRecord.objects.all()
#             print('Existing Accessrecords')
#             d = {'accessrecords': LOA}
#             return render(request, 'Display_access.HTML', d)
#         else:
#             return HttpResponse('Accessrecord is already present')
        
#     else:
#         return HttpResponse('Webpage is not present')      
    


# def display_topic(request):
#     LOT = Topic.objects.all()
#     # LOT = Topic.objects.filter(topic_name__startswith = 'C')
#     # LOT = Topic.objects.filter(topic_name__endswith='l')
#     # LOT = Topic.objects.filter(topic_name__contains='cr')
#     # LOT = Topic.objects.filter(topic_name__regex='^F\w+')
#     d = {'topics': LOT}
#     return render(request, 'Display_Topic.HTML', d)

# def display_webpage(request):
#     LOW = Webpage.objects.all()
    
#     # LOW = Webpage.objects.filter(pk__in=(1,5))
    
#     # LOW = Webpage.objects.filter(pk__range=(1,5))
#     # LOW = Webpage.objects.filter(pk__gt = 3)
#     # LOW = Webpage.objects.filter(pk__lt = 3)
#     # LOW = Webpage.objects.filter(pk__lte = 3)
#     # LOW = Webpage.objects.filter(pk__gte = 5)

#     d = {'webpages': LOW}
#     return render(request, 'Display_webpage.HTML', d) 

# def display_Accessrecord(request):
#     LOA = AccessRecord.objects.all()
#     # LOA = AccessRecord.objects.filter(date = '1999-03-12')
#     # LOA = AccessRecord.objects.filter(date__month = 7)
#     # LOA = AccessRecord.objects.filter(date__day = 12)
#     LOA = AccessRecord.objects.filter(date__year= 1999) 
#     d = {'accessrecords': LOA}
#     return render(request, 'Display_access.HTML', d)
              