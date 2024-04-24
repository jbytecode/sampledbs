function docalculations(){
    let txt_a = document.getElementById("txt_a");
    let txt_b = document.getElementById("txt_b");
    let txt_c = document.getElementById("txt_c");

    let div_delta = document.getElementById("delta");
    let div_x1 = document.getElementById("x1");
    let div_x2 = document.getElementById("x2");

    let a = parseFloat(txt_a.value);
    let b = parseFloat(txt_b.value);
    let c = parseFloat(txt_c.value);

    let delta = b * b - 4 * a * c;

    let x1 = (-b + Math.sqrt(delta)) / (2 * a);
    
    let x2 = (-b - Math.sqrt(delta)) / (2 * a);

    div_delta.innerHTML = delta;
    div_x1.innerHTML = x1;
    div_x2.innerHTML = x2;
}