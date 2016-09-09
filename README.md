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
