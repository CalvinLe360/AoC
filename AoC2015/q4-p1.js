md5 = require('js-md5');
let input = "ckczppom";

let hash = "12345"
let integer = 0;

while(hash.substring(0, 5) != "00000"){
    hash = md5(input + integer);
    integer++;
}

integer--;
console.log(integer, hash);