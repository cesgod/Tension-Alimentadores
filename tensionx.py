#!/usr/bin/env python3
from re import I
from zeep import Client
from zeep import xsd
from datetime import date, datetime, timedelta
import datetime
import json
#import numpy as np




#currentMonth = datetime.now().month


with open('/var/www/html/santa/stereq.json', 'r') as f:
    rangeib = json.load(f)
nlim=len(rangeib)
for i in range(nlim):
    day1 	= int(rangeib['range01']['day1'])
    day1s 	= int(rangeib['range01']['day1s'])
    month1 	= int(rangeib['range01']['month1'])
    month1s = int(rangeib['range01']['month1s'])
    year1 	= int(rangeib['range01']['year1'])
    year1s	= int(rangeib['range01']['year1s'])
    day2 	= int(rangeib['range01']['day2'])
    month2 	= int(rangeib['range01']['month2'])
    year2 	= int(rangeib['range01']['year2'])
    #meterd 	= rangeib['range01']['meter']

print(day1, month1, year1, day2, month2, year2)

maxdata=0
lastlimit=0
timestamp=""
f_date = date(year1, month1, day1)
l_date = date(year2, month2, day2)
delta = l_date - f_date
print("days in between: ", delta.days)
#meter = meterd
bwsdl = "http://clvmweb.clyfsa.com:81/SEP2WebServices/DataService.svc?singleWsdl"
bclient = Client(bwsdl)
minute="00"
hour=0
sminute=""
alldvcs=[]
hcount=0
months=month1
days=0
month2=str(month2)
if (len(month2)==1):
	month2="0"+month2
#if (day1!= 1):
	#days=day1-1
#else:
	#days=30
	#months=month1-1

hib=0
mlen=len(minute)
cc=0

month1s=str(month1s)
if (len(month1s)==1):
	month1s="0"+month1s
#hlen=len(hour)
day1s=str(day1s)
day1=str(day1)
month1=str(month1)
if (len(day1s)==1):
	day1s="0"+day1s
if (len(month1)==1):
	month1="0"+month1


#month2
month2=str(month2)
if (len(month2)==1):
	month2="0"+month2
#hlen=len(hour)
day2=str(day2)
if (len(day2)==1):
	day2="0"+day2


startdate = str(year1s)+"-"+month1s+"-"+day1s+"T03:00:00"
sminute = str(year2)+"-"+month2+"-"+day2+"T03:00:00"
print(startdate)
print(sminute)
print(mlen)
print(day1, len(day1))
wlimit=(delta.days+1)*96
print("limite: ",wlimit)





#print(currentMonth)
wsdl = "http://clvmweb.clyfsa.com:81/SEP2WebServices/ManagementService.svc?singleWsdl"
client = Client(wsdl)



#request_data ={
#    "groupReference": {
#      "Name": "PDS EXCLUSIVOS Activos",
#    } 
#  }
#response = client.service.QueryGroupMembers(**request_data)

request ={
    "groupReference": {
      "Name": "Active-MT880",
    }
  }
response = client.service.QueryGroupMembers(**request)
#print (response)
#Here 'request_data' is the request parameter dictionary.
#Assuming that the operation named 'sendData' is defined in the passed wsdl.
#print (response)
#lim = len(response["Devices"]["DeviceReference"])
print(response)
limamt = len(response["Devices"]["DeviceReference"])

flim=limamt
devices_all= []
devices_conn=[]
devices_rconn=[]
allmtsc=[]
allmtsr=[]
counter=1
ndvcs=[]
l1maxd=''
l2maxd=''
l3maxd=''
l1mind=''
l2mind=''
l3mind=''
#for j in range (lim):
#	devices_all.append(response["Devices"]["DeviceReference"][j]["Name"])
for k in range (limamt):
	devices_all.append(response["Devices"]["DeviceReference"][k]["Name"])

lim = len(devices_all)
dconn   =   0
conn    =   0
wsdl = "http://clvmweb.clyfsa.com:81/SEP2WebServices/DataService.svc?singleWsdl"
client = Client(wsdl)

#x=296
for x in range (50):
	#print(response["Devices"]["DeviceReference"][x]["Name"])  

	bwsdl = "http://clvmweb.clyfsa.com:81/SEP2WebServices/DataService.svc?singleWsdl"
	bclient = Client(bwsdl)

	brequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": response["Devices"]["DeviceReference"][x]["Name"],
	        "AgencyId": "0",
	        "ResultTypeNames":  "ActivePowerComb(|+A|+|-A|)_INST_LP1",
	        
	      }
	    },
	    "intervalStart": startdate,
	    "intervalEnd": sminute,
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "false"
	  }

	#bresponse = bclient.service.QueryResults(**brequest_data)
	crequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": response["Devices"]["DeviceReference"][x]["Name"],
	        "AgencyId": "0",
	        "ResultTypeNames": "Voltage_L1_INST_LP2"
	      }
	    },
	    "intervalStart": startdate,
	    "intervalEnd": sminute,
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "false"
	  }

	#cresponse = bclient.service.QueryResults(**crequest_data)
	drequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": response["Devices"]["DeviceReference"][x]["Name"],
	        "AgencyId": "0",
	        "ResultTypeNames": "Voltage_L2_INST_LP2"
	      }
	    },
	    "intervalStart": startdate,
	    "intervalEnd": sminute,
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "false"
	  }
	#dresponse = bclient.service.QueryResults(**drequest_data)
	#alldvcs.append(cresponse)
	erequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": response["Devices"]["DeviceReference"][x]["Name"],
	        "AgencyId": "0",
	        "ResultTypeNames": "Voltage_L3_INST_LP2"
	      }
	    },
	    "intervalStart": startdate,
	    "intervalEnd": sminute,
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "false"
	  }

	#print(aresponse)
	#bresponse = bclient.service.QueryResults(**brequest_data)
	#print(bresponse)
	cresponse = bclient.service.QueryResults(**crequest_data)
	dresponse = bclient.service.QueryResults(**drequest_data)
	eresponse = bclient.service.QueryResults(**erequest_data)
	#alldvcs.append(aresponse)
	#alldvcs.append(bresponse)
	#alldvcs.append(cresponse)
	#alldvcs.append(dresponse)
	#alldvcs.append(eresponse)
	#alldvcs.append(response["Devices"]["DeviceReference"][x]["Name"])
	
	#alldvcs.append(aresponse[0]['Attributes']['AttributeInfo'][6]['Value']['Value'])
	
	#print(aresponse[0]['Attributes']['AttributeInfo'][7]['Value']['Value'])
	#if hasattr(bresponse[0].ResultsByResultType, 'ResultTypeResults'):
	#	if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
	#		if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
	#			alldvcs.append(bresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value)
	#		else:
	#			alldvcs.append('n/a')
	#	else:
	#		alldvcs.append('n/a')
	#else:
	#	alldvcs.append('n/a')	
	#print(cresponse)
	#print(dresponse)
	#print(eresponse)
	#print(response["Devices"]["DeviceReference"][x]["Name"])
	if (cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results'] == None or  dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results'] == None or eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results'] == None):
		print("xdxd")
	else:	
		alldvcs.append({'MeterName':response["Devices"]["DeviceReference"][x]["Name"]})
		lastlimit=len(cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'])
		#print(response["Devices"]["DeviceReference"][x]["Name"])
		counter=counter+1
		#print(counter)
		
		#print(alldvcs)
		maxdata=0
		timestamp=""
		l1max=cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][x]['Value']['Value']
		l2max=dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][x]['Value']['Value']
		l3max=eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][x]['Value']['Value']
		l1min=cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][x]['Value']['Value']
		l2min=dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][x]['Value']['Value']
		l3min=eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][x]['Value']['Value']
		for i in range(lastlimit):			
			if hasattr(cresponse[0].ResultsByResultType, 'ResultTypeResults'):
				if hasattr(cresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
					if hasattr(cresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
						#print(x)
						#print(i)
						if (cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']>l1max):
							l1max=cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['L1MAX']=cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['DateL1MAX']= (cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Timestamp'] - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M")
						if (cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']<l1min):
							l1min=cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['L1MIN']=cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['DateL1MIN']= (cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Timestamp'] - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M")
						#if len(ndvcs) != lastlimit:
							#ndvcs[x].append(cresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value'])
							#alldvcs=cresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[i].Value.Value
							#alldvcs=((cresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Timestamp - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M"))
							#alldvcs.append(cresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value)


					else:
						alldvcs.append('n/a')
				else:
					alldvcs.append('n/a')
			else:
				alldvcs.append('n/a')	
			if hasattr(dresponse[0].ResultsByResultType, 'ResultTypeResults'):
				if hasattr(dresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
					if hasattr(dresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
						if (dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']<l2max):
							l2max=dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['L2MAX']=dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['DateL2MAX']=(dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Timestamp'] - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M")
						if (dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']<l2min):
							l2min=dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['L2MIN']=dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['DateL2MIN']= (dresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Timestamp'] - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M")
						#alldvcs=dresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
						#alldvcs=((dresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Timestamp - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M"))
						#alldvcs.append(dresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value)
					else:
						alldvcs.append('n/a')
				else:
					alldvcs.append('n/a')
			else:
				alldvcs.append('n/a')	
			if hasattr(eresponse[0].ResultsByResultType, 'ResultTypeResults'):
				if hasattr(eresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
					if hasattr(eresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
						if (eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']>l3max):
							l3max=eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['L3MAX']=eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['DateL3MAX']= (eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Timestamp'] - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M")
						if (eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']<l3min):
							l3min=eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['L3MIN']=eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Value']['Value']
							alldvcs[x]['DateL3MIN']= (eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Timestamp'] - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M")
						#alldvcs.append({'MeterName':response["Devices"]["DeviceReference"][x]["Name"]})
						#alldvcs.append({'Date': (eresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][i]['Timestamp'] - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M")})
						#alldvcs=eresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
						#alldvcs=((eresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Timestamp - timedelta(hours=3)).strftime("%d-%m-%Y %H:%M"))
						#alldvcs.append(eresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value)
					else:
						alldvcs.append('n/a')
				else:
					alldvcs.append('n/a')
			else:
				alldvcs.append('n/a')		
			#if hasattr(eresponse[0].ResultsByResultType, 'ResultTypeResults'):
			#	if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			#		if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
						
			#			dateasd= str(bresponse[0]['ResultsByResultType']['ResultTypeResults'][0]['Results']['Result'][0]['Timestamp'])
			#			alldvcs.append(dateasd)
			#		else:
			#			alldvcs.append('n/a')
			#	else:
			#		alldvcs.append('n/a')
			#else:
			#	alldvcs.append('n/a')	
				
			#print(bresponse[0]["ResultsByResultType"]["ResultTypeResults"][0]["Results"]["Result"][0]["Value"]["Value"])
			#alldvcs.append('NOPE')
			#ele = (input("Name : ")) 
			#d = json.loads(s)
#print (alldvcs)
#print(ndvcs)
with open('/var/www/html/santa/data.json', 'w', encoding='utf-8') as f:
    json.dump(alldvcs, f, ensure_ascii=False, indent=4)

	# prints [1,3,5]    
#aresponse = aclient.service.QueryDeviceAttributes(**raequest_data)

#print (alldvcs)
