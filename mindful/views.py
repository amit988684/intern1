from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from json import dumps
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
# Create your views here.
import urllib

def test_form_collection(request):
    if request.method == 'GET':
        return render(request, 'profileForm.html')

    elif request.method == 'POST':
        # r = urllib.urlopen('http://127.0.0.1:5000/').read()
        # soup = BeautifulSoup(r, 'html.parser')

        #profile
        first_name = request.POST['first_name']
        # print(first_name)
        # first_name = soup.find('span', attrs={'name': 'first_name'})
        last_name= request.POST['last_name']
        auth_url = 'http://awsdev.globalhuntindia.com/Candi/'

        headers = {'content-type':'application/json'}
        # payload={'canId':canId.text,'aadharCardNo':'','age':'','area_of_specialization':'','first_name':first_name.text,'last_name':last_name.text,'candidate_name':first_name.text + ''+last_name.text,'category':category.text,'communicationrating':'','confidential':'','createdDate':'','createdUserID':'','createdBy':'','dob':dob.text,'summary':summary.text,'emp_status_c':'','exNationality':'','fedrated':'','functionText':'','gender':gender.text,'hotNotes':'','hourly_rate':'','imageName':'','imgPhoto':imgPhoto['src'],'industryText':industryText.text,'job_description':job_description.text,'job_type':job_type.text,'language':'','lastModifiedUserID':'','modifiedby':'','lastUpdateDate':'','mobile':mobile.text,'maritalStatus':maritalStatus.text,'nationality_c':'','notes':'','noticePeriod':'','officePh':'','officePhExt':'','pANNo':'','passportNo':'','passportValidity':'','perferLocation':perferLocation.text,'phoneH':'','differentlyAbled':differentlyAbled.text,'differentlyAbled_type':'','phychallenged':'','pref_distance':'','reason_change':'','reason_relocate':'','references_1':'','references_2':'','releventExp':'','relocate':'','res_headline':headline.text,'searchsheet':'','shift_work':'','sLL_Number':'','source':'','subFunctionText':'','subIndustryText':'','willing_to_relocate':'','willingToChangeJob':'','workingFrom':'','originalFileName':'','modifiedFileName':'','resume':resume.text,'fresher':'','email':{'primary':email_id.text,'secondary':'','third':'','fourth':'','fifth':''},'skill':{'skills':{'lastUsed':'','expirence':'','text':skills.text},'one':{'lastUsed':'','expirence':'','text':one.text},'two':{'lastUsed':'','expirence':'','text':two.text},'three':{'lastUsed':'','expirence':'','text':three.text},'four':{'lastUsed':'','expirence':'','text':four.text},'five':{'lastUsed':'','expirence':'','text':five.text}},'address':{'permanentAddress':{'country':country.text,'city':city.text,'street':'','location':'','state':'','pincode':''},'currentAddress':{'country':'','city':'','street':'','location':'','state':'','pincode':''}},'education':{'ug':{'degree':degree.text,'degree_type':degree_type.text,'course':course.text,'institute':institute.text,'university':institute.text,'from_where':from_where.text,'to':ugto.text,'year':ugyear.text,'percentage':'','eduDetails':''},'pg':{'degree':'','degree_type':'','course':'','institute':'','university':'','from_where':'','to':'','year':'','percentage':'','eduDetails':''},'doctorate':{'year':'','percentage':'','course':'','institute':'','eduDetails':''},'tength':{'school':'','specification':'','city':'','board':'','from_where':'','to':'','year':'','percentage':'','eduDetails':''},'diploma':{'year':'','percentage':'','course':'','institute':'','eduDetails':''},'twelveth':{'school':twelthschool.text,'specification':twelthspecification.text,'city':twelthcity.text,'board':'','from_where':'','to':twelthto.text,'year':twelthyear.text,'percentage':'','eduDetails':''},'certificates':{'certificates_title':'','certificates_from':'','certificates_to':'','certificates_description':''}},'employment':{'current':{'workLocation':workLocation.text,'role':role.text,'level':'','teamSize':'','organization':organization.text,'designation':designation.text,'current_city':current_city.text,'current_from': current_from.text,'present_date':present_date.text,'current_description':current_description.text},'previous':{'organization1':'','organization':'','organization2':'','organization3':'','organization4':'','designation':'','previous_city':'','previous_from':'','previous_to':'','previous_description':''},'achievement':{'achievement_title':'','achievement_from':'','achievement_to':'','achievement_description':''}},'project':{'project_title':project_title.text,'project_role':project_role.text,'project_from':project_from.text,'project_to':project_to.text,'url':project_url.text,'project_description':project_description.text},'salary':{'negotiableCTC':'','presentCTC':'','type_of':'','expectedCTC':expectedCTC.text,'presentCTC_type':'','expectedCTC_type':''},'experience':{'months':'','TotalExp':experience.text,'years':experience.text}}
        body={'first_name':first_name,'last_name':last_name}
        r = requests.post(auth_url,data=body)
        t = requests.get(url=auth_url)
        print (r.status_code)
        print(t.content)
        return HttpResponseRedirect('http://127.0.0.1:5000/')
