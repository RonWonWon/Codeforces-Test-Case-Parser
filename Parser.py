import requests
from bs4 import BeautifulSoup

inp = input().split();
ID = inp[0]; p = inp[1];

url = "https://codeforces.com/contest/"+ID+"/problem/"+" "+p;
page = requests.get(url);

soup = BeautifulSoup(page.content, "html.parser");

results = soup.find("div", class_ = "sample-tests");

inputs = [];
outputs = [];

var = results.text;
arr = var.split('\n');
parity = 0;
j = 1;
while(j<len(arr)):
	s = "";
	while(j<len(arr) and arr[j]!="Input" and arr[j]!="Output"):
		s += arr[j]+'\n'; 
		j += 1;
	if(parity==0):
		inputs.append(s);
	else:
		outputs.append(s);
	s = "";
	parity ^= 1;
	j += 1;
	
N = len(inputs);
for i in range(0,N):
	i1 = "input"+str(i+1)+".txt";
	o1 = "output"+str(i+1)+".txt";
	f1 = open(i1,'w');
	f2 = open(o1,'w');
	f1.write(inputs[i]);
	f2.write(outputs[i]);
