let input = "R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3"
input = input.split(", ")

let x = 0
let y = 0
let direction = 0

let visited = {}
let visited_twice = false
visited["0,0"] = true

for(let i = 0; i < input.length; i++){
    if(input[i][0] == 'L'){
        direction = (4 + direction - 1) % 4
    }
    else {
        direction = (direction + 1) % 4
    }

    let move_count = Number(input[i].substring(1))
    let cy = y
    let cx = x
    switch(direction){
        case 0:
            for(let j = cy+1; j <= cy + move_count; j++){
                if(visited[x+","+j] == true) visited_twice = true
                y++;
                visited[x+","+j] = true
                console.log(x,y)

                if(visited_twice) break;
            }
            break;
        case 1:
            for(let j = cx+1; j <= cx + move_count; j++){
                if(visited[j+","+y] == true) visited_twice = true
                x++;
                visited[j+","+y] = true
                console.log(x,y)

                if(visited_twice) break;
            }
            break;
        case 2:
            for(let j = cy-1; j >= cy - move_count; j--){
                if(visited[x+","+j] == true) visited_twice = true
                y--;
                visited[x+","+j] = true
                console.log(x,y)

                if(visited_twice) break;
            }
            break;
        case 3:
            for(let j = cx-1; j >= cx - move_count; j--){
                if(visited[j+","+y] == true) visited_twice = true
                x--;
                visited[j+","+y] = true
                console.log(x,y)

                if(visited_twice) break;
            }
            break;
    }

    console.log(visited_twice)
    if(visited_twice) break;
}

console.log(Math.abs(x) + Math.abs(y), x, y)