const input = [
    "RUDULRLLUULRURDDRRUDURULLLDRLRLUDDLUDUDDUDRRDUDULDUUULLRULLRLDDLDLDDRLRRRRUDLLDDUULDRLLUDDRRUURLULRRRDLLURRUUDURUDDURLUDDDLUDDUUDUURUDLRDRDRLRDRLDRUDRUUDLRDDRRURDDLRDDRRURDUDDLULLUDRURURRRLRRUDUULULULRRLDLUDUURRLLRUDLLDRDDLRRRULRUDLULDDLLLULDLRUDLLLLRDDLRDRLDRLLRDRRDLRDULULRLLLDRUDRRRUULRUULDRURLUDRURRDLLDLRDLDDDDRRLUDLRRLUUUURDRDDLRRURURRDUULLRLURLURUDDDRDURDUUDRLRLRRLDDLDLDLDDDUDDULURLDDLLRLRRDULUDDLULRLUDDLDLRULUUUDRLDRUDURLUDDRLLRUULDLRRRRDLLLLURULLRDRRUDLUULRRDLLRLRLUDLDDULLDLLRDLDLL",
    "LLUUUUUUDUDRLRDRDLDURRRLLRRLRURLLUURRLLUDUDLULUURUUURDLUDLDDLULLRDLRUULDLRDUDURLLDDUDUDULLUDDUULLLUULRRRLULRURRDLRUDUDDURRRDRUURDURLLULLRULLDRUULLURLDRDUUDDDDDDRRLDRLRRRLULDDUURRLLLLDRURLURDRDRDURUDUURRDUDUDRLLUUDDRLUDDDRDLDLRLDRURRDLLRULDRLLURURRLUULLRLRRURDDRDRUUURUURUUUDLLRRLUDRLDLRLURLDLUDDUDDDLDUDRRLDLRURULRLLRDUULURRRULDLLLRLDDDUURRRRDULLRURRLULULDLRRUDUDDLRUURDLDUDDUDRRDLRRRDUDUUUDLLDDDDLURLURRRUUULLLULRRLLLLLLULDUUDLRUDRRDLRDUUDUDLLRLDLLRUURDUUURUUUDDLLUUDLULDURLULULUUUDRUDULLURRULRULLRDLDDU",
    "RLUUURULLDLRLDUDRDURRDUURLLUDDDUULRRRLRLURDDRUULUDULDUUDDDDUDDDDRUDDLDUUDRUDLRRRLLRDDLLLRLLRUULRUULDDRURRLURRLRLULDDRRRDDURDDRDRDULRUDRUUDULRLLULDLRLLDRULRDDRRDDUDLRLLUDRDRRRLUDULRDLRDDURRUUDDRRUDURRUUUDDRRDUDURLUUDUDUURDDDLURLULLUULULURUDUUDRUDULLUUULURDLDUULLDDLLDULRLRLRDUUURUUDLRLDURUDRLDULLUDLDLLRDUURRDUDURLUUUDLLRRULRLULRLDLLURDURRULRLLRRDUDLLRDRRRRDLUUDRUUUDDLRLUDDDDDDRURRRUUURRDLLRURLDDLLDLRRLLLDRRULRRUDLDRDDRRLULURLLUURURURRRRUUUUURUDURLRLLLULULDLLDLRDRRULUDUDRDRRDRDRRDUDLLLRUDRUDDDULRULRRRDRLRUUUURUDURDUUULLULRUDDULDUUDLDURRD",
    "ULRULDDLDLULLLRRRLRUDDDDDLLDDUDLRRDULUUDRDLRRURDRRLUULRURUDRRULDLLLUDRUUDULULUDDRUDDDRDURRRDRDUUURLRDULUDRDRLDRUDDLLLDRRULUDLUDLDLLRRUDUULULDLDLLUURDLDDLLUUDURLURLLLDRDLDRRLRULUURRDRULRUUURULRRUDDDDLLDLDDLLRRLRRRRDUUDUDLDRDRRURDLRURULDLRDLLLLRUDRLLRDLRLRDURDRUDURRRLRDRDLLRLUDDDDRLRLLDUURRURLUURUULUDLUURDRRUDDLUDUDDDURRDRUDRLRULDULUUUUUUDDUDRUDUUURUDRRDLUDLUUDUULUDURDLDDDLLURRURUUDUDDRRDRLLULULDRLRURRDDDRDUUURDDDRULUDRDDLDURRLDDDLRRRLDDRDURULDLUDLLLURLURRLRRULDLLDDUDRRULDRRRRLURRUULRRRUDLURDLLDLLDULUUDRRLDLLLDRLRUDLUULDLDRUDUDURDRUDRDDDLRLULLUR",
    "LRLUUURRLRRRRRUURRLLULRLULLDLUDLUDRDDRLDLRLULLURDURLURDLLRLDUUDDURRRRLDLLRULLRLDLLUUDRLDDLLDRULDRLLRURDLRURRUDLULLRURDLURRURUDULLDRLLUUULUDRURRUUDUDULUUULRLDDULDRDLUDDUDDDLRURULLDLLLRLLUURDLRUDLLLLDLLRLRUUUDDRUUUUDLDLRDDURLDURUULLLUUDLLLLDULRRRLLDLDRRDRLUDRUDURLLUDLRLLUDUDRDDDRDLRDLRULUULDRLUDLRLDUURLRRLUDDDUUDDDUDRLDLDUDLURUULLDDDURUUULRLUDLDURUUDRDRURUDDUURDUUUDLLDLDLDURUURLLLLRURUURURULRULLRUDLRRUUUUUDRRLLRDDUURDRDRDDDUDRLURDRRRUDLLLDURDLUUDLLUDDULUUDLDUUULLDRDLRURUURRDURRDLURRRRLLUUULRDULDDLDUURRDLDLLULRRLLUDLDUDLUUL"
]

let password = ""

var x = 1
var y = 1
for(let i = 0; i < input.length; i++){
    for(let inst_ind = 0; inst_ind < input[i].length; inst_ind++){
        switch(input[i][inst_ind]){
            case 'U':
                y = Math.max(y-1, 0)
                break;
            case 'D':
                y = Math.min(y+1, 2)
                break;
            case 'L':
                x = Math.max(x-1, 0)
                break;
            case 'R':
                x = Math.min(x+1, 2)
                break;
        }
    }
    
    let key = y*3 + x+1
    password += key
}

console.log(password)