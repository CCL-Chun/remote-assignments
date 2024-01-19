function max(numbers){
    // first check the input have at least one number and no other types
    if(numbers.length < 1 || !numbers.every(Number.isInteger)){
        return "Please give me array with only numbers!"
    }
    let start = 1; // start from 1
    var num = numbers[0]; // set the first element
    while(start < numbers.length){
        if(num < numbers[start]){
            num = numbers[start]; // renew a larger num 
            start++; // step to next element
        } else{
            start++; // step to next element
        }
    }
    return num; // return the max num
}

console.log(max([9,3,5,"fregvgf"])) // test