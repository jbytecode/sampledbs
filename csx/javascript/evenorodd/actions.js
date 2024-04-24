function sayevenorodd(){
    let txt_number = document.getElementById("txt_number");

    let number = parseInt(txt_number.value);

    let result = "";

    if (number % 2 == 0) {
        result = "Even";
    } else {
        result = "Odd";
    }

    document.getElementById("div_result").innerHTML = result;
}

