<h1>Knight Sequences</h1>

Pictured below is a keypad:



We want to find all 10-key sequences that can be keyed into the keypad in the following manner:
<br> <br>
<div style = "margin-left:60px;">
•	The initial keypress can be any of the keys. <br>
•	Each subsequent keypress must be a knight move from the previous keypress.   <br>
•	There can be at most 2 vowels in the sequence. <br>
•	We will attempt to run your solution at lengths of 10, 16 and 32.<br>
</div>
<br><br>
A knight move is made in one of the following ways:<br><div style = "margin-left:60px;">
1.	Move two steps horizontally and one step vertically.<br>
2.	Move two steps vertically and one step horizontally.<br>
</div>
There is no wrapping allowed on a knight move.

KeyBoard

         ['A','B','C','D','E'],
         ['F','G','H','I','J'],
         ['K','L','M','N','O'],
         ['1','2','3']

              ]






Your program should first write the number of valid 10-key sequences on a single line to standard out.  


<h1> To Use </h1>

Simply call the function start with two variables. The first which letter you want to start at and how many letters you want the password to be. Such that: <br><br>

 starter('A',5)

 <br><br>

 Will yield:

 <br><br>

 ['ALCLC', 'ALCF1', 'ALCFM', 'ALCFC', 'AH1H1', 'AH1HK', 'AH1F1', 'AH1FM', 'AH1FC', 'AHK2K', 'AHK2G', 'AHKH1', 'AHKHK', 'AHKBM', 'AHKBK']


 <h1> Planning and Discussion </h1>

 The methods I used worked to trim run time. I used Python's generator functions to make the iterations run as fast as python would allow. Given production level implementation what I would do would be to populate a running graph that tracked the connections between the letters. I would make every query fill out a multi-child graph representation of the data. Such that once all of the connections where made the algorithm would simply traverse the graph rather than build a new iteration of the function every time.
