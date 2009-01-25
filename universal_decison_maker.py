#!/usr/bin/python

import random
from time import sleep
again = "yes"
while again is "yes":
	print "Welcome to the universal decision maker, may I take your order?"
	order = raw_input("Please input a decision to make: ")
	yes_no = random.choice(["yes", "no", "maybe"])
	print "Please wait while we calculate decision..."
	sleep(15)
	print "The answer to '" + str(order) + "' is " + str(yes_no) +"."
	again = raw_input("Make another decision?(yes or no): ")

if again == "no":
	print "Come again soon."
	exit()
