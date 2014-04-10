from django.shortcuts import render_to_response
from courses.models import Course, Section, Professor
# Create your views here.
def index(request):
    if request.method == 'GET':
        print("GET called")
    return render_to_response('search/search_index.html')

def search_prof(request):
    return render_to_response('search/search_prof.html')

def search_course(request):
    return render_to_response('search/search_course.html')

def search_sections(request):
    return render_to_response('search/search_sections.html')

def initiate_prof_search(request):
    prof_listing = []
    args={}
    if request.GET.get('name'):
        args['name__contains']= request.GET.get('name')
    if request.GET.get('department'):
        args['department__dep_name__contains']= request.GET.get('department')
    if request.GET.get('ratings'):
        args['rating_value'] = request.GET.get('ratings')
    if request.GET.get('quality'):
        args['easiness_value'] = request.GET.get('quality')
    if request.GET.get('easiness'):
        args['easiness'] = request.GET.get('easiness')
    professors = Professor.objects.filter(**args)

    profs = []
    for prof in professors:
        profs.append(prof)    
    dict = {"professors": profs}

    '''
    for professor in professors:
        prof_dict = {}
        prof_dict['professor_object'] = professor
        prof_dict['name']=professor.name
        prof_dict['university']=professor.university.university_name
        prof_dict['rating_value']=professor.rating_value
        prof_dict['easiness_value']=professor.easiness_value
        prof_dict['department']=[ x.dep_name for x in professor.department.all()]
        prof_listing.append(prof_dict)
    '''
    return render_to_response('search/professor_results.html',dict)

def initiate_course_search(request):
    course_listing = []
    args={}
    if request.GET.get('name'):
        args['course__course_name__contains']=request.GET.get('name')
    if request.GET.get('course_id'):
        args['course__course_id']=request.GET.get('course_id')
    if request.GET.get('registration_code'):
        args['registration_code']=request.GET.get('registration_code')
    if request.GET.get('university'):
        args['course__university__university_name__contains'] = request.GET.get('university')
    if request.GET.get('department'):
        args['course__department__contains'] = request.GET.get('department')
    if request.GET.get('professor'):
        args['professor__name__contains'] = request.GET.get('professor')

    sections = Section.objects.filter(**args)
    course_sections = {}
    for section in sections:
        if section.course in course_sections:
            course_sections[section.course] = course_sections[section.course].append(section)
        else:
            course_sections[section.course] = [section]

    dict = {"courses" : course_sections}
    return render_to_response('search/courses_results.html', dict)
    '''
    for section in sections:
        course_dict = {}
        course_dict['section_object'] = section
        course_dict['course_object'] = section.course
        course_dict['name'] = section.course.course_name
        course_dict['course_id'] = section.course.course_id
        course_dict['university'] = section.course.university.university_name
        course_dict['department'] = section.course.department.dep_name
        course_dict['registration_code'] = section.registration_code
        course_dict['section_id']=section.section_id
        course_dict['professor']= [prof.name for prof in section.professor.all()]
        course_dict['location']=section.location
        course_dict['location2']=section.location2
        course_dict['class_type']=section.class_type
        course_dict['class_type2']=section.class_type2
        course_dict['time']=section.time
        course_dict['time2']=section.time2
        course_dict['days']=section.days
        course_dict['days2']=section.days2
        course_dict['date_range']=section.date_range
        course_dict['date_range2']=section.date_range2

        course_listing.append(course_dict)

    return render_to_response('search/course_results.html', course_listing)
    '''
