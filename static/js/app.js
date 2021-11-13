// HTML Elements
const returnDiv = document.querySelector('.return');
const summaryDiv = document.querySelector('.summary');
const resetDiv = document.querySelector('.reset');
const cellDivs = document.querySelectorAll('.game-cell');
const playerScore = document.querySelector('.player-score');
const computerScore = document.querySelector('.computer-score');
const drawScore = document.querySelector('.draws');
const totalGames = document.querySelector('.total-games');

var game = {
    playerTurn: true,
    gameIsLive: true,
    player: 'x',
    computer: 'o',
    gameBoard: [' ',' ',' ',' ',' ',' ',' ',' ',' '],
    scorePlayer: 0,
    scoreComputer: 0,
    scoreDraw: 0,
    gamesTotal: 0,
}


//functions
const handleReturn = (e) => {
    history.back();
}

const handleSummary = (e) => {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("overlay").style.pointerEvents = "all";
}

const exitSummary = (e) => {
    document.getElementById("overlay").style.display = "none";
}

const handleReset = (e) => {
    for (const cellDiv of cellDivs) {
        cellDiv.classList.remove('x');
        cellDiv.classList.remove('o');
        cellDiv.classList.remove('won');
    }
    game['gameIsLive'] = true;
    playerScore.innerHTML = `Player Score: ${game['scorePlayer']}`;
    computerScore.innerHTML = `Computer Score: ${game['scoreComputer']}`;
    drawScore.innerHTML = `Draws: ${game['scoreDraw']}`;
    totalGames.innerHTML = `Total Games Played: ${game['gamesTotal']}`;
    resetBoard();

    // replace with the one who wins will start
    game['playerTurn'] = true;
}

const resetBoard = () => {
    game['gameBoard'] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
}

const handleCellClick = (e) => {
    const classList = e.target.classList;
    const pos = classList[1]
    const cellNo = getIndexCell(pos)

    if(classList[2] == 'x' || classList[2] == 'o') {
        return;
    }

    if(!game['gameIsLive']) {
        console.log(game['gameIsLive'])
        return;
    }

    if (game['playerTurn'] == true) {
        classList.add(game['player'])
        game['gameBoard'][cellNo] = game['player']
        game['playerTurn'] = false
        checkGameStatus()
    }

    calculateComputerMove()
}

// Returns index of cell clicked
const getIndexCell = (pos) => {
    if(pos == 'top-left') {
        return 0; }
    if(pos == 'top-center') {
        return 1; }
    if(pos == 'top-right') {
        return 2; }
    if(pos == 'middle-left') {
        return 3; }
    if(pos == 'middle-center') {
        return 4; }
    if(pos == 'middle-right') {
        return 5; }
    if(pos == 'bottom-left') {
        return 6; }
    if(pos == 'bottom-center') {
        return 7; }
    if(pos == 'bottom-right') {
        return 8; }
}

// Check for wins
const checkGameStatus = () => {
    const topLeft = cellDivs[0].classList[2];
    const topCent = cellDivs[1].classList[2];
    const topRight = cellDivs[2].classList[2];
    const midLeft = cellDivs[3].classList[2];
    const midCent = cellDivs[4].classList[2];
    const midRight = cellDivs[5].classList[2];
    const botLeft = cellDivs[6].classList[2];
    const botCent = cellDivs[7].classList[2];
    const botRight = cellDivs[8].classList[2];

    //Horizontal Win
    if(topLeft && topLeft == topCent && topLeft == topRight ) {
        handleWin(topLeft,0,1,2);
        return;
    }
    else if(midLeft && midLeft == midCent && midLeft == midRight ) {
        handleWin(midLeft,3,4,5);
        return;
    }
    else if(botLeft && botLeft == botCent && botLeft == botRight ) {
        handleWin(botLeft,6,7,8);
        return;
    }

    //Vertical Win
    else if(topLeft && topLeft == midLeft && topLeft == botLeft ) {
        handleWin(topLeft,0,3,6);
        return;
    }
    else if(topCent && topCent == midCent && topCent == botCent ) {
        handleWin(topCent,1,4,7);
        return;
    }
    else if(topRight && topRight == midRight && topRight == botRight ) {
        handleWin(topRight,2,5,8);
        return;
    }

    //Diagonal Win
    if(topLeft && topLeft == midCent && topLeft == botRight ) {
        handleWin(topLeft,0,4,8);
        return;
    }
    if(topRight && topRight == midCent && topRight == botLeft ) {
        handleWin(topRight,2,4,6);
        return;
    }
    
    // Tie
    if(!boardEmpty()) {
        handleTie()
    }
}

// Update color of winning combination and scores
const handleWin = (mark, cell1, cell2, cell3) => {
    game['gameIsLive'] = false;
    cellDivs[cell1].classList.add('won')
    cellDivs[cell2].classList.add('won')
    cellDivs[cell3].classList.add('won')

    if(mark == 'x') {
        game['scorePlayer'] = game['scorePlayer'] + 1;
        game['gamesTotal'] = game['gamesTotal'] + 1;
    }
    else {
        game['scoreComputer'] = game['scoreComputer'] +  1;
        game['gamesTotal'] = game['gamesTotal'] + 1;
    }
}

// Returns true if board is empty 
const boardEmpty = () => {
    for (const cell of game['gameBoard']) {
        if (cell == ' ') {
            return true
        }
    }
    return false
}

// Update Tie function
const handleTie = () => {
    game['gameIsLive'] = false;
    game['scoreDraw'] = game['scoreDraw'] + 1;
    game['gamesTotal'] = game['gamesTotal'] + 1;
}

//event handlers
returnDiv.addEventListener('click', handleReturn);
summaryDiv.addEventListener('click', handleSummary);
window.addEventListener('mouseup', exitSummary);
resetDiv.addEventListener('click', handleReset);

for (const cellDiv of cellDivs) {
    cellDiv.addEventListener('click',handleCellClick);
}

// Send a request to calculate computer move
const calculateComputerMove = () => {

    if (game['gameIsLive'] == false) {
        return;
    }

    const data = JSON.stringify({'board':game['gameBoard'], 'computer':game['computer'], 'player':game['player']})
    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/play/move')
    xhr.setRequestHeader("Content-Type","application/json");
    xhr.onreadystatechange = comMove
    xhr.send(data)
}

// Update the board according to response
function comMove() {
    if(this.readyState == 4 && this.status == 200) {      
        response = JSON.parse(this.responseText)
        cellNo = response['computerMove']
        console.log(cellNo)
        if(cellNo == -1) {
            return;
        }
        const classList = cellDivs[cellNo].classList
        classList.add(game['computer']);
        game['gameBoard'][cellNo] = game['computer']
        game['playerTurn'] = !game['playerTurn']
        checkGameStatus()
    }
}