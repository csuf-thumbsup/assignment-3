# assignment-3

Given the following text file "data.txt". Write a program to copy the file into file "newdata.txt" by removing all comment lines (lines that begin with //), blank lines, extra spaces before and after each token (leave one space before and one after each token)

####"data.txt" file
    //declare variables
    int   num1,   nume2, num3 ,t;
    
    //initialize variables 
    num1  =3;  num2 =  5  ;
    	num3   =     7   ;
    //compute and display their total
    t=   num1  +  num2;//compute num1+num2
    t   =   t+num3; //compute new value for tl
    
    cout<<  t  ;
    
####"newdata.txt"
    int num1 , nume2 , num3 , t ;
    num1 = 3 ;
    num2 = 5 ;
    num3 = 7 ;
    t = num1 + num2 ;
    t = t + num3 ;
    cout<< t ;    
    
    
--
###Results from my attempt at Assignment 3;
    int num1 , nume2 , num3 , t;
    num1 = 3; num2 = 5 ;
    num3 = 7 ;
    t = num1 + num2;
    t = t + num3;
    cout<< t ;


I refactored my code and its way way cleaner and easier to follow through plus it goes about beautifying the input in a simpler way. If you still want to check out my explanation for the old version of the code then just look at the [old.README.md](https://github.com/csuf-thumbsup/assignment-3/blob/Michael/old.README.md). Same goes for the [old.Main.py](https://github.com/csuf-thumbsup/assignment-3/blob/Michael/old.Main.py).

I still have issues with multiple semi-colons per line and am trying to figure it out... but I'm sure you guys will come up with the answer in c++. 

