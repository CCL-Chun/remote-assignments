function findPosition(numbers,target){
    // first check the input have at least one number and no other types
    if(numbers.length < 1 || !numbers.every(Number.isInteger)){
        return "Please give me array with only numbers!"
    }
    let start = 0; // start from 0
    while(start < numbers.length){
        if(target !== numbers[start]){
            start++; // go to next number
        } else{
            return start; // return the index
        } 
    }
    return -1; // find no target in numbers
}

console.log(findPosition([3,4,2,1,6,7,4,0],4))