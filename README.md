# Sudoku Solver Visualizer
Simple application to visualize the mechanism of backtracking algorithm in solving Sudoku puzzles

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Mechanism](#mechanism)
* [Screenshots](#screenshots)
* [Status](#status)
* [Contributors](#contributors)

## General info
This project is finished in one or two days during my 2020 summer. I was learning to implement the backtracking algorithm, which leverages the power of **recursion** technique in enumerating and testing all possible solutions before choosing the correct one. After understanding how backtracking works, I decided to visualize it by making an application, preferably a desktop app. The main backtracking algorithms is implemented using Python behind the scenes and HTML, CSS and JavaScript will be on the frontend. To connect the two sides, I use a Python library called [**Eel**](https://pypi.org/project/Eel/). You can read about it using the link I provided. In this repository, I have explained everything you need to know before using the application. 

## Technologies
- Python
- HTML
- CSS
- JavaScript
- Eel Python Library

## Mechanism
In this section, I will not go in details about how backtracking algorithm works but I want to elaborate more on the structure of the program and how I visualized it. I also assume that you know the mechanism of Sudoku game. Let's go !

Firstly, I want to give a brief overview to our main connector, **Eel** library. According to its documentation, Eel is a little Python library for making simple Electron-like offline HTML/JS GUI apps, with full access to Python capabilities and libraries. Eel hosts a local webserver, then lets you annotate functions in Python so that they can be called from Javascript, and vice versa. 

In the root directory, I created a **main.py** file that containing implementation for backtracking algorithms and some required functions that are exposed to other JS files through the library. As the same folder hierarchy with the main python file, I created a folder called **public** containing all the HTML/JS files which are responsible for visualizing the algorithm. 

In the **main.py** file, there is a default board of default level easy, which is a 2 dimensional list. On application starting up, the JS file will call a function in Python file to output to the screen a square for every element in the list, which are 9x9 squares in total. The **solve** function will be the main function implementing the algorithm. For every square in the board, the algorithm will test a value range from 1 to 9. If the value is valid, it will temporarily put the number to that square and do same thing to the next empty square. So every time it found a presumably valid value for the square, it will change the background color of that square to green. Similaryly, if there is a case when there is no valid value for that square, the background color will be red. During this process, you won't be able to do some tasks such as generating a new board because it might crash the system. I also created three default sudoku boards of level easy, medium and hard. You can choose which level you want the application to solve. Additionally, you can also change the speed at which the algorithm is visualized, which basically changes the number of seconds the program will delay for every trying-out-and-assigning-value step.

Because the application is using a local host on port 2000 on your computer so during its runtime, you cannot start up a new application using the same port. Given a test case that you generate a hard sudoku puzzle and set the visualization speed to slow then you will have to wait for it to finish visualizing the solution before start it up again, even if you are able to close it. Closing the application with the solver still visualizing underground will make a crash on your next app startup since the port is being allocated for the unfinished app task. Of course, this needs to be improved but I want to make this simple and showcase what I have learnt. 

I also included a Windows executable file to help you test it out. Feel free to download and try it yourself. Cheers !

## Screenshots
![Sudoku1](https://github.com/DNT-Khoa/Advanced-Project-for-Housing-Agency/blob/master/images/Login%20Page%20Housemate.PNG)

## Status: 
Completed

## Contributors:
- Georgie Nikolov
- Khoa Doan
- Daniel Vaswani
