from django.shortcuts import render
from portfolio.models import Aboutme,Offering,Myprojects,Myskils,Myexperience,Workingstyle,Uploadcv
# Create your views here.
def home(request):
    template_name = "index.html"
    datas = Aboutme.objects.all()
    skills=Myskils.objects.all()
    offers =Offering.objects.all()
    myexperience=Myexperience.objects.all()
    all_datas = Myprojects.objects.all().order_by("project_name")[:3]
    working_style =Workingstyle.objects.all()

    context={"datas":datas,"skills":skills,
    "offers":offers,"myexperience":myexperience,
    "all_datas":all_datas,"working_style":working_style}
    #print(context)
    # for i in  data:
    #     context ={
    
    #     "name":i.name,
    #     "post":i.post,
    #     "dob":i.dob,
    #     "phone_no":i.phone_no,
    #     "pic":i.pic,
    #     "email":i.email,
    #     "address":i.address,
    #     "fb_address":i.fb_address,
    #     "insta_address":i.insta_address,
    #     "linkdin_id":i.linkdin_id,
    #     "github_id":i.github_id,
    #     "twitter_id":i.twitter_id,
    #     "aboutme":i.aboutme,
    # }
    return render (request,template_name,context)

def aboutme(request):
    template_name= 'aboutme.html',
    datas = Aboutme.objects.all()
    context ={'datas':datas}
    # for i in  data:
    #     context ={
    
    #     "name":i.name,
    #     "post":i.post,
    #     "dob":i.dob,
    #     "phone_no":i.phone_no,
    #     "pic":i.pic,
    #     "email":i.email,
    #     "address":i.address,
    #     "fb_address":i.fb_address,
    #     "insta_address":i.insta_address,
    #     "linkdin_id":i.linkdin_id,
    #     "github_id":i.github_id,
    #     "twitter_id":i.twitter_id,
    #     "aboutme":i.aboutme,

    # }
    # #print(context)
    return render(request,template_name,context)
def services(request):
    template_name = "services.html"
    offers =Offering.objects.all()
    datas = Aboutme.objects.all()
    context ={"datas":datas,"offers":offers}
    # for i in  data:
    #     context ={
    
    #     "name":i.name,
    #     "post":i.post,
    #     "dob":i.dob,
    #     "phone_no":i.phone_no,
    #     "pic":i.pic,
    #     "email":i.email,
    #     "address":i.address,
    #     "fb_address":i.fb_address,
    #     "insta_address":i.insta_address,
    #     "linkdin_id":i.linkdin_id,
    #     "github_id":i.github_id,
    #     "twitter_id":i.twitter_id,
    #     "aboutme":i.aboutme,

    # }
    return render(request,template_name,context)
def contactme(request):
    template_name = "contact.html"
    datas = Aboutme.objects.all()
    context ={"datas":datas}
    # for i in  data:
    #     context ={
    
    #     "name":i.name,
    #     "post":i.post,
    #     "dob":i.dob,
    #     "phone_no":i.phone_no,
    #     "pic":i.pic,
    #     "email":i.email,
    #     "address":i.address,
    #     "fb_address":i.fb_address,
    #     "insta_address":i.insta_address,
    #     "linkdin_id":i.linkdin_id,
    #     "github_id":i.github_id,
    #     "twitter_id":i.twitter_id,
    #     "aboutme":i.aboutme,

    # }
    return render(request,template_name,context)
def projects(request):
    template_name = "portfolio.html"
    datas = Aboutme.objects.all()
    all_datas = Myprojects.objects.all()
    context ={"datas":datas,"all_datas":all_datas}
    
    return render(request,template_name,context)
def uploadcv(request):
    template_name = "cv.html"
    datas = Aboutme.objects.all()
    cv = Uploadcv.objects.all()
    context = {"datas":datas,"cv":cv }
    return render(request,template_name,context)



