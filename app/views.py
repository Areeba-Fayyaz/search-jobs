from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import pyrebase


config={
    "apiKey": "AIzaSyC7YhphbDCb6raG40HIl0SGE7sK5wS4U4Q",
  "authDomain": "cpanel-1bd11.firebaseapp.com",
  "projectId": "cpanel-1bd11",
  "storageBucket": "cpanel-1bd11.appspot.com",
  "messagingSenderId": "611467979075",
  "appId": "1:611467979075:web:36a25358545436d9d6a7f6",
  "measurementId": "G-ZBPP8ZW2WF",
  "databaseURL":"https://cpanel-1bd11-default-rtdb.firebaseio.com/"
	

}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
comb_lis=[]

# move to this search.html page to search for content
def search(request):
	return render(request, "search.html")

	

# after typing what to search this function will be called
def searchusers(request):
	value = request.POST.get('search')
	print(value)
	
	# if no value is given then render to search.h6tml
	if value =="":
		return render(request, "search.html")
        
	else:
		data = database.child('users').shallow().get().val()
		print(data,"======================================")
		
		uidlist = []
		
			
		for i in data:
			print(i)
			uidlist.append(i)
				
			# if we have find all the uid then
			# we will look for the one we need
		value=value.lower()
		value=value.split(' ')
		jobdescriptions=[]
		companynamelist=[]
		for i in uidlist:
			val = database.child('users').child(i).child('jobdescription').get().val()
			val=val.lower()
				
			for item in value:
				if item in val  :
					print('found++++++++++++++++++++++++++++++++++++++++++++++++++')
					print(i)
					if val not in jobdescriptions:
						jobdescriptions.append(val)
						companynamelist.append(i)
			

				# print(val,value)
		print(len(jobdescriptions))
		comb_lis = zip(jobdescriptions,companynamelist)
			
		return render(request, "search.html", {"comb_lis": comb_lis})

				

				
	
			


# Create your views here.
# def index( request):
#     # return HttpResponse("this is homepage")
#     # auth.logout(request)
#     return render(request,'firebase.html')
# def about( request):
#     return HttpResponse("this is aboutpage")
# def services( request):
#     return HttpResponse("this is servicespage")
# def contacts( request):
#     return HttpResponse("this iscontactspage")

