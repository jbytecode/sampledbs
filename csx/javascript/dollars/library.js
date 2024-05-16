const dollars = new Array(100).fill(100);

const init = () => {
  console.log('Library initialized');
  drawDollars();
}

const reset = () => {   
    dollars.fill(100);
    drawDollars();
    printDollars();
}

const transaction = () => {
    // Draw random integer from 0 to 100
    let randomIndex1 = Math.floor(Math.random() * 100);
    let randomIndex2 = Math.floor(Math.random() * 100);
    if (dollars[randomIndex1] > 0) {
        dollars[randomIndex1]--;
        dollars[randomIndex2]++;
    }
}

const drawDollars = () => {
    // HTMLCanvasElement
    let canvas = document.getElementById('dollarsCanvas');

    // CanvasRenderingContext2D
    let ctx = canvas.getContext('2d');
    let width = canvas.width;
    let height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    let step = width/100;

    var dollarindex = 0;
    for (let i = 0; i < width; i+=step) {
        let x = i;
        let y = height - dollars[dollarindex];
        ctx.beginPath();
        ctx.rect(x, y, step, dollars[dollarindex]);
        ctx.closePath();
        ctx.stroke();
        dollarindex++;
    }
}

const printDollars = () => {
    const txtOutput = document.getElementById("txtOutput");
    txtOutput.value = dollars.toString().replace(/,/g, ", ");
}

const simulate = () => {
    var maxval = parseInt(document.getElementById("txtStep").value);
    for (let i = 0; i < maxval; i++) {
        transaction();
    }
    drawDollars();
    printDollars();
}


