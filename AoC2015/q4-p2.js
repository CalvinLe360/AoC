md5 = require('js-md5');
let input = "ckczppom";

let hash = "123456"
let integer = 117946;

while(hash.substring(0, 6) != "000000"){
    hash = md5(input + integer);
    integer++;
}

integer--;
console.log(integer, hash);