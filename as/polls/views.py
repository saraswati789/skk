from django.shortcuts import render
import MySQLdb
db=MySQLdb.connect('localhost','root','','mnnit')
cur=db.cursor()
def index(request):
	return render(request, 'polls/index.html');
	cur.execute('insert into table1 values("nm","pas")');
	if request.GET.get('q'):
		nm=request.GET['nm']
		pas=request.GET['pass']	
		with db:
			cur.execute('insert into table1 values(nm,pas)');
		return render(request, 'polls/a.html');