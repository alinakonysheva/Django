from django.urls import path
from mycv.views import do_home, do_search, do_experience, do_experience_add, do_skills, do_skill, do_skill_add, do_most_used

app_name = 'mycv' 
urlpatterns = [
    path('', do_home, name='do_home'),
    path('search/', do_search, name='do_search'),
    path('experience/<int:experience_id>', do_experience, name='do_experience'),
    path('experience/', do_experience_add, name='do_experience_add'),   
    path('skills/', do_skills, name='do_skills'),
    path('skill/<int:skill_id>', do_skill, name='do_skill'),
    path('skill/', do_skill_add, name='do_skill_add'),
    path('most-used/', do_most_used, name='do_most_used'),    
]