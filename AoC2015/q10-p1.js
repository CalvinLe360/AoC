let input = "1113222113"

for(let i = 0; i < 40; i++){
    console.log(input)
    input = execute(input)
}

function execute(let_input){
    let value = let_input[0]
    let count = 1
    let new_string = ""

    for(let j = 0; j < let_input.length; j++){
        if(let_input[j] == value) count++
        else {
            new_string += count
            new_string += value
            value = let_input[j];
            count = 1
        }
    }

    return new_string
}

console.log(input.length)