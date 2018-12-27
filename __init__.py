import subprocess
from flask import Flask,render_template
app = Flask(__name__, template_folder='templates')

def det_actual_time():
        file_actual_time=open("/var/www/yoyokoyo/actual_time.txt", "r")
        for line in file_actual_time:
                actual_time = line[0:-8]
        return actual_time

def listing_of_cve():
        file_cve=open("/var/www/yoyokoyo/lines_of_cve.txt", "r")
        list_of_cve=[]
        for line in file_cve:
                list_of_cve.append(line)
        return list_of_cve

def listing_of_dates():
        file_dates=open("/var/www/yoyokoyo/lines_of_dates.txt", "r")
        list_of_dates=[]
        for line in file_dates:
                list_of_dates.append(line)
        o=0
        for date in list_of_dates:
                list_of_dates[o]=date[:-8]
                o+=1
        return list_of_dates



def listing_of_desc():
        file_desc=open("/var/www/yoyokoyo/lines_of_desc.txt", "r")
        list_of_desc=[]
        for line in file_desc:
                list_of_desc.append(line)
        return list_of_desc

def find_the_right_cve():
        actual_time = det_actual_time()
        list_of_dates = listing_of_dates()
        index_actual_date = [i for i, x in enumerate(list_of_dates) if x == actual_time]
	#print(index_actual_date)
	list_of_cve = listing_of_cve()
	list_of_actual_cve=[]
	for k in index_actual_date:
		list_of_actual_cve.append(list_of_cve[k])
	#print(list_of_actual_cve)
	return list_of_actual_cve

def find_the_right_desc():
        actual_time = det_actual_time()
        list_of_dates = listing_of_dates()
        index_actual_date = [i for i, x in enumerate(list_of_dates) if x == actual_time]
        list_of_desc = listing_of_desc()
        list_of_actual_desc=[]
        for k in index_actual_date:
        	list_of_actual_desc.append(list_of_desc[k])
        return list_of_actual_desc

actual_time = det_actual_time()
list_of_actual_cve = find_the_right_cve()
list_of_actual_desc = find_the_right_desc()
length_list=len(list_of_actual_cve)


@app.route("/")
def hello():
        return render_template('home.html',list_of_actual_cve=list_of_actual_cve,list_of_actual_desc=list_of_actual_desc,length_list=length_list,actual_time=actual_time)

if __name__ == "__main__":
    app.run()
