var level = "Easy";
var speed = "Slow";

const mySudoku = document.getElementById('my-sudoku');

eel.expose(generateBox);
function generateBox(val, y = 0, x = 0) {
    // Create a square and add the box class to it
    const boxDiv = document.createElement("div");
    boxDiv.classList.add("box");

    // Add identifier class to the square
    let identifier = y.toString() + x.toString();
    boxDiv.classList.add(identifier);

    // Append box to the sudoku board
    if (val !== 0) {
        boxDiv.innerText = val;
    }
    mySudoku.append(boxDiv);
}

function setDefaultBoard() {
    for (var i = 0; i < 81; i++) {
        generateBox(0);
    }
}


function generateBoard() {
    mySudoku.innerHTML = '';
    eel.generateNewBoard(level);
    eel.print_board_to_web();
}


function solveBoard() {
    // mySudoku.innerHTML = '';
    disableGenerateButton();
    eel.solve(speed);
    // eel.print_board_to_web()
}

// This function will visualize the process of trying and eliminating values
eel.expose(updateSquareValue);
function updateSquareValue(y, x, val) {
    let identifier = y.toString() + x.toString();
    let square = document.getElementsByClassName(identifier)[0];
    if (val !== 0) {
        square.style.backgroundColor = "#ADFFAF";
        square.style.transform = "translate(2px)";
        square.style.boxShadow = "-5px 5px 20px rgba(87, 233, 8, .85)";
        square.style.color = "black";

        square.innerText = val;

    } else {
        square.style.backgroundColor = "#e43f5a";
        square.style.boxShadow = "-5px 5px 20px rgba(249, 6, 59, .85)";
        square.style.color = "white";
    }

    setTimeout( () => {
        square.style.transform = "";
        square.style.boxShadow = "";
    }, 150);
}

// Set the default board
// setDefaultBoard()


function chooseLevel(levelInp) {
    const levelBar = document.getElementsByClassName("level-bar")[0];
    levelBar.innerText = levelInp;
    level = levelInp;
}

function chooseSpeed(speedInp) {
    const speedBar = document.getElementsByClassName("speed-bar")[0];
    speedBar.innerText = speedInp;
    speed = speedInp;
}

eel.expose(disableGenerateButton);
function disableGenerateButton() {
    const generateBtn = document.getElementById("generate-btn");
    generateBtn.disabled = true;
}

eel.expose(enableGenerateButton);
function enableGenerateButton() {
    const generateBtn = document.getElementById("generate-btn");
    generateBtn.disabled = false;
}