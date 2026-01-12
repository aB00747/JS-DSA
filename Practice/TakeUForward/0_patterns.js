// let n = 5;
// let str = ""

// for (let i = 0; i <= n; i++) {
//     str += "* "
// }

// console.log(str)


function printStar(n) {

    let str = "";

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            str += "*";
        }

        str += "\n";
    }

    return str;
}

// console.log(printStar(5))


function printTriangleStar(n) {
    let str = "";

    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= i; j++) {
            str += "*";
        }

        str += "\n";
    }

    return str;
}

// console.log(printTriangleStar(4))

function printNumberTriangle(n) {
    let str = "";

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= i; j++) {
            str += j;
        }

        str += "\n";
    }

    return str;
}

// console.log(printNumberTriangle(5))

function printRowNumberPattern(n) {
    let str = "";

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= i; j++) {
            str += i;
        }

        str += "\n";
    }

    return str;
}

// console.log(printRowNumberPattern(5));

function printReverTriangleStar(n) {
    let str = "";

    for (let i = 0; i < n; i++) {
        for (let j = n - i; j > 0; j--) {
            str += "*";
        }

        str += "\n"
    }

    return str;
}

// console.log(printReverTriangleStar(5));



function printReverTraingleNum(n) {
    let str = "";

    for (let i = 0; i < n; i++) {
        for (let j = 1; j < n - i + 1; j++) {
            str += j;
        }

        str += "\n"
    }

    return str;
}

console.log(printReverTraingleNum(5));



function  printPyramidStar(n) {
    let str = "";

    for (let i = 0; i < n; i++) {
        // space
        for (let j = 0; j < n - i - 1; j++) {
            str += " ";
        }

        // star
        for (let j = 0; j < 2 * i  + 1; j++) {
            str += "*";
        }

        // space
        for (let j = 0; j < n - i - 1; j++) {
            str += " ";
        }

        str += "\n";
    }

    return str;
}

// console.log(printPyramidStar(5));


function printRevPyramidStar(n) {
    let str = "";

    for (let i = 0; i < n; i++) {
        // space
        for (j = 0; j < i; j++) {
            str += " ";
        }

        // star
        for (let j = 0; j < 2 * (n - i) - 1; j++) {
            str += "*";
        }

        // space
        for (j = 0; j < i; j++) {
            str += " ";
        }

        str += "\n";
    }

    return str;
}


console.log(printRevPyramidStar(5));

// Desclaimer - This is the MATRIX - Consider after learned MATRIX to solve this
// Print a pattern of numbers from  to  as shown below. Each of the numbers is separated by a single space.
//      0 1 2 3 4 5 6
    //  ^ ^ ^ ^ ^ ^ ^
// 0 -> 4 4 4 4 4 4 4  
// 1 -> 4 3 3 3 3 3 4   
// 2 -> 4 3 2 2 2 3 4   
// 3 -> 4 3 2 1 2 3 4   
// 4 -> 4 3 2 2 2 3 4   
// 5 -> 4 3 3 3 3 3 4   
// 6 -> 4 4 4 4 4 4 4 
function printNnum(n) {
    let str = "";
    const len = 2 * n - 1;

    for (let i = 0; i < len; i++) {
        const row = [];
        for (let j = 0; j < len; j++) {
            const top = i;
            const left = j;
            const bottom = len - 1 - i;
            const right = len - 1 - j;
            const minDist = Math.min(top, left, bottom, right);
            row.push(n - minDist);
        }
        str += row.join(" ") + "\n";
    }

    return str;
}

console.log(printNnum(4))



function symetricPattern(n) {
    let str = "";

    for(i = 1; i <= 2 * n - 1; i++) {
        let stars = i;

        if (i > n) {
            stars = 2 * n - i;
        }

        for (j = 1; j <= stars; j++) {
            // console.log("*");
            str += "*"
        }

        str += "\n";
    }

    return str;
}




function zeroOne(n) {
    let str = "";
    let start  = 1;

    for (let i = 0; i < n; i++) {
        
        if (i % 2 == 0) {
            start = 1;
        } else {
            start = 0;
        }

        for (let j =  0; j <= i; j++) {
            // str += start
            // start = start == 0 ? 1 : 0;
            str += start;
            start = 1 - start;
        }

        str += "\n";

    }

    return str;
}

console.log(zeroOne(5)) 


