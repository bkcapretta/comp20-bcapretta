import os

word = 'hey'
while True:
	word += 'y'
	os.system('curl --data "username=' + word +'&lat=40&lng=40" "https://gentle-sands-25039.herokuapp.com/submit"');

