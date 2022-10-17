#!/usr/bin/python3
""" A module to get info from an api"""
import requests
import sys

if __name__ == "__main__":
	complete = 0
	task_list = []
	response_task = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(sys.argv[1]))
	total = len(response_task.json())
	response_user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1]))
	username = response_user.json().get("name", None)
	for i in response_task.json():
		if i.get("completed", False):
			complete += 1
			task_list.append(i.get("title", None))
	print("Employee {} is done with tasks({:d}/{:d}):".format(username, complete, total))
	for i in task_list:
		print("\t {}".format(i))
