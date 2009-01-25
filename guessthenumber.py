diff --git a/guessthenumber.py b/guessthenumber.py
deleted file mode 100644
index e9f8feb..0000000
--- a/guessthenumber.py
+++ /dev/null
@@ -1,41 +0,0 @@
-#!/usr/bin/env python
-
-import random
-import urllib
-
-print "Let's play 'Guess the number'"
-print "You win if you guess the number in 10 turns or less"
-number = random.randint(1,1000)
-guesses = input("Please insert a number: ")
-turn = 0
-print 'Current guess: ' + str(guesses)
-
-while guesses < number:
-	print "Number is greater than current guess."
-	guesses = input("Please insert a number greater than current guess: ")
-	turn += 1
-while guesses > number:
-	print "Number is less than current guess."
-	guesses = input("Please insert a number less than current guess: ")
-	turn += 1
-while guesses is 100 > number:
-	print "Number is much less than current guess."
-	guesses = input("Please insert a number less than current guess: ")
-	turn += 1 
-while guesses is 100 < number:
-	print "Number is much more than current guess."
-	guesses = input("Please insert a number more than current guess: ")
-	turn += 1 
-
-if guesses == number:
-	if turn < 10:
-		print "You win!!! You guessed the number in " + str(turn) +" turns"
-		exit()
-
-	if turn == 10:
-		print "You win!!! You guessed the number in " + str(turn) +" turns"
-		exit()
-
-	if turn > 10:
-		print "You lose... You guessed the number in " + str(turn) +" turns"
-		exit()
