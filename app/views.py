from django.shortcuts import render,HttpResponse
# from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import pyrebase


# import { initializeApp } from "firebase/app";
# import { getAnalytics } from "firebase/analytics";
# const firebaseConfig = {
#   apiKey: "AIzaSyC7YhphbDCb6raG40HIl0SGE7sK5wS4U4Q",
#   authDomain: "cpanel-1bd11.firebaseapp.com",
#   projectId: "cpanel-1bd11",
#   storageBucket: "cpanel-1bd11.appspot.com",
#   messagingSenderId: "611467979075",
#   appId: "1:611467979075:web:36a25358545436d9d6a7f6",
#   measurementId: "G-ZBPP8ZW2WF"
# };


# const app = initializeApp(firebaseConfig);
# const analytics = getAnalytics(app);


config={
    "apiKey": "AIzaSyC7YhphbDCb6raG40HIl0SGE7sK5wS4U4Q",
  "authDomain": "cpanel-1bd11.firebaseapp.com",
  "projectId": "cpanel-1bd11",
  "storageBucket": "cpanel-1bd11.appspot.com",
  "messagingSenderId": "611467979075",
  "appId": "1:611467979075:web:36a25358545436d9d6a7f6",
  "measurementId": "G-ZBPP8ZW2WF",
  "databaseURL":"https://cpanel-1bd11-default-rtdb.firebaseio.com/"
	
	# "databaseURL": "https://console.firebase.google.com/project/cpanel-1bd11/database/cpanel-1bd11-default-rtdb/data/~2F",
	# "projectId": "cpanel-1bd11",

}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
comb_lis=[]

# move to this search.html page to search for content
def search(request):
	# user=authe.create_user_with_email_and_password("areeba","1234")
	# uid=user["localId"]
	# data={"name":"areeba","status":"1"}
	# database.child("users").child(uid).child("details")
	return render(request, "search.html")
# def createDB(request):
	

# after typing what to search this function will be called
def searchusers(request):
	value = request.POST.get('search')
	print(value)
	
	# if no value is given then render to search.h6tml
	if value =="":
		return render(request, "search.html")
        
	# title = request.POST['category']
	# if title =="":
	# 	return render(request, "search.html")
	# if value is None or title is None:
	# 	print(value ,"Value",title)
	# 	return render(request, "search.html")
	else:
		# if title == "Users":
		data = database.child('users').shallow().get().val()
		print(data,"======================================")
		
		uidlist = []
		requid = 'null'
			
	# 		# append all the id in uidlist
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

				

				
	# 			# if uid we want is value then
	# 			# we will store that in requid
	# 			if (val == value):
	# 				requid = i
	# 		if requid=='null':
	# 			return render(request, "search.html")
	# 		print(requid)
			
	# 		# then we will retrieve all the data related to that uid
	# 		name = database.child('users').child(requid).child('name').get().val()
	# 		course = database.child('users').child(requid).child('course').get().val()
	# 		branch = database.child('users').child(requid).child('branch').get().val()
	# 		img = database.child('users').child(requid).child('imgUrl').get().val()
	# 		Name = []
	# 		Name.append(name)
	# 		Course = []
	# 		Course.append(course)
	# 		Branch = []
	# 		Branch.append(branch)
	# 		Image = []
	# 		Image.append(img)
	
			
	# 		# send all data in zip form to searchusers.html
			
	# return render (request,"data.html")


# Create your views here.
def index( request):
    # return HttpResponse("this is homepage")
    # auth.logout(request)
    return render(request,'firebase.html')
def about( request):
    return HttpResponse("this is aboutpage")
def services( request):
    return HttpResponse("this is servicespage")
def contacts( request):
    return HttpResponse("this iscontactspage")

