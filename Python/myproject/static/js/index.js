row1col1 = document.getElementById('row1col1');
row1col2 = document.getElementById('row1col2');
row1col3 = document.getElementById('row1col3');

row2col1 = document.getElementById('row2col1');
row2col2 = document.getElementById('row2col2');
row2col3 = document.getElementById('row2col3');

row3col1 = document.getElementById('row3col1');
row3col2 = document.getElementById('row3col2');
row3col3 = document.getElementById('row3col3');

var WhatIsAntValue = 0;
function ChangeValue() {
    if (WhatIsAntValue == 0) {
        WhatIsAntValue = 1
    } else {
        WhatIsAntValue = 0
    }
}

var matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];


function addValue(event) {
    var id = event.target.id;
    col = id[3]
    row = id[7]
    imgElement = document.createElement('img');
    if (WhatIsAntValue == 0) {
        imgElement.src = './static/imgs/x.png'
        imgElement.alt = 'X'
        var valueName = 1
    } else {
        imgElement.src = './static/imgs/bola.png'
        imgElement.alt = 'Bola'
        var valueName = 2
    }
    

    imgElement.style.maxWidth = '100%';
    imgElement.style.maxHeight = '100%';

    id = document.getElementById(id)

    var checkIfImg = id.querySelector('img') !== null;

    if (checkIfImg) {
        alert('Ja tem um valor aqui')
    } else {
        id.appendChild(imgElement);
        if (valueName == 1) {
            matriz[col-1][row-1] = 1
        } else {
            matriz[col-1][row-1] = 2
        }
        ChangeValue()
    }
    List1 = []
    List2 = []
    List3 = []
    List4 = []
    List5 = []

    List4.push(matriz[0][0])
    List4.push(matriz[1][1])
    List4.push(matriz[2][2])
    List5.push(matriz[0][2])
    List5.push(matriz[1][1])
    List5.push(matriz[2][0])

    for (let Number = 0; Number < 3; Number++) {
        if (JSON.stringify(matriz[Number]) === JSON.stringify([1, 1, 1]) || JSON.stringify(matriz[Number]) === JSON.stringify([2, 2, 2])) {
            alert('Jogo terminado')
            location.reload();
        } 
        for (let Number2 = 0; Number2 < 3; Number2++) {
            if (Number2 == 0) {
                List1.push(matriz[Number][Number2])
            }
            if (Number2 == 1) {
                List2.push(matriz[Number][Number2])
            }
            if (Number2 == 2) {
                List3.push(matriz[Number][Number2])
            }
        }
         if (JSON.stringify(List1) === JSON.stringify([1, 1, 1]) || JSON.stringify(List1) === JSON.stringify([2, 2, 2])) {
            alert('Jogo terminado')
            location.reload();
        } else if  (JSON.stringify(List2) === JSON.stringify([1, 1, 1]) || JSON.stringify(List2) === JSON.stringify([2, 2, 2])) {
            alert('Jogo terminado')
            location.reload();
        } else if  (JSON.stringify(List3) === JSON.stringify([1, 1, 1]) || JSON.stringify(List3) === JSON.stringify([2, 2, 2])) {
            alert('Jogo terminado')
            location.reload();
        } else if (JSON.stringify(List4) === JSON.stringify([1, 1, 1]) || JSON.stringify(List4) === JSON.stringify([2, 2, 2])) {
            alert('Jogo terminado')
            location.reload();
            break
        } else if (JSON.stringify(List5) === JSON.stringify([1, 1, 1]) || JSON.stringify(List5) === JSON.stringify([2, 2, 2])) {
            alert('Jogo terminado')
            location.reload();
            break
        }
    }

}
