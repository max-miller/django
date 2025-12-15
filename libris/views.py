from django.shortcuts import render
from .models import annual_reviews


editions = list(annual_reviews.objects.order_by('edition_number'
                                                ).values_list('edition_number', flat=True).distinct())
#
#
# Create your views here.
def index(request):

    return render(request,"book_index.html",{'editions':[{'number': n, 'label': f'Edition{n}'} for n in editions]}
                  )
#
#
#
def letter(request, edition_name):
    edition_n = int(''.join(char for char in edition_name if char.isdigit()))
    edition_content = list(annual_reviews.objects.filter(edition_number=edition_n).values())
    edition_content = [{'title':book['title'],'author':book['author'],'cover_img_link':book['cover_img_link'],
                        'review':book['review'].split('<p>')} for book in edition_content]
    return render(request, 'letter_template.html',{'editions':[{'number': n, 'label': f'Edition{n}'} for n in editions],
                                                   'edition_content':edition_content,
                                                   'edition_n':edition_n,
                                                   })
