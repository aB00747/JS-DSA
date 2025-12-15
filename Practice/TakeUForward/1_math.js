/**
 * Return all divisors of a number in ascending order.
 *
 * If `n` is falsy (0, null, undefined), the function returns `0`.
 * Note: This implementation begins `i` at 0 (consistent with original
 * code). Passing `0` will short-circuit above; for positive integers the
 * function collects "small" divisors and corresponding "large" divisors
 * (via n / i), then concatenates them into a sorted list.
 *
 * @param {number} n - The positive integer to list divisors for.
 * @returns {number[]|number} An array of divisors (ascending) or `0` when `n` is falsy.
 * @example
 * // returns [1,2,3,4,6,9,12,18,36]
 * printDivisor(36);
 */
function printDivisor(n) {
    if (!n) return 0

    let i = 0;
    let small = [];
    let large = [];

    while (i * i <= n) {
        if (n % i == 0) {
            small.push(i);

            if (i != n / i) {
                large.push(n / i);
            }
        }

        i++;
    }

    large.reverse();

    let result = [...small, ...large]

    return result;
}


// console.log("printDivisor", printDivisor(36));


/**
 * Count how many digits of `n` divide `n` evenly.
 *
 * If `n` is falsy the function returns `0`.
 * The function examines each decimal digit of `n` (least-significant first)
 * and increments the count when `original % digit === 0`.
 * Digits equal to `0` are not counted because `original % 0` yields `NaN`.
 *
 * @param {number} n - The positive integer whose digits will be checked.
 * @returns {number} The count of digits that evenly divide the original number.
 * @example
 * // The digits of 121 that divide 121 are 1 and 1 -> returns 2
 * countDigitDivisor(121);
 */
function countDigitDivisor(n) {
    if (!n) return 0;

    let count = 0;
    let ld = 0;
    let original = n;

    while (n > 0) {
        ld = n % 10;

        if (original % ld == 0) {
            count++;
        }

        n = Math.floor(n / 10);
    }

    return count;
}

console.log("countDigitDivisor", countDigitDivisor(121));

/**
 * Determine whether a number is prime.
 *
 * If `n` is falsy the function returns `false`.
 * This routine counts divisors by checking up to sqrt(n) and accounting for
 * both factors in each pair; if the total divisor count equals 2 the
 * number is prime.
 *
 * @param {number} n - The integer to check for primality.
 * @returns {boolean} `true` if `n` is prime, otherwise `false`.
 * @example
 * // returns true
 * isPrimeNumber(11);
 */
function isPrimeNumber(n) {
    if (!n) return false;

    let count = 0;
    let i = 1;

    while (i * i <= n) {
        if (n % i == 0) {
            count++


            if (n / i != i) {
                count++;
            }
        }

        i++
    }

    if (count == 2) {
        return true;
    } else {
        return false
    }
}

// console.log("isPrimeNumber is 11", isPrimeNumber(11))



/**
 * Compute the greatest common divisor (GCD) of two numbers using a brute-force scan.
 *
 * If either `n1` or `n2` is falsy the function returns `0`.
 * This implementation checks every integer from `1` up to `min(n1, n2)` and
 * tracks the largest common divisor found.
 *
 * @param {number} n1 - First positive integer.
 * @param {number} n2 - Second positive integer.
 * @returns {number} The greatest common divisor of `n1` and `n2`.
 * @example
 * // returns 10
 * gcdNumber(20, 10);
 */
function gcdNumber(n1, n2) {
    if (!n1 || !n2) return 0;

    let gcd = 1;
    let i = 1;

    while (i <= Math.min(n1, n2)) {
        if (n1 % i == 0 && n2 % i == 0) {
            gcd = i;
        }

        i++;
    }

    return gcd;

}


// optimze way

/**
 * Compute the greatest common divisor (GCD) of two numbers by scanning downwards
 * from the smaller value to 0 and returning the first common divisor found.
 *
 * If either `n1` or `n2` is falsy the function returns `0`.
 * Note: This function mirrors the original implementation which uses an
 * undeclared loop variable `i` (global leak). The JSDoc documents intended
 * behavior but does not change the function body.
 *
 * @param {number} n1 - First positive integer.
 * @param {number} n2 - Second positive integer.
 * @returns {number} The greatest common divisor of `n1` and `n2`.
 * @example
 * // returns 20
 * gcdOptimze(20, 40);
 */
function gcdOptimze(n1, n2) {
    if (!n1 || !n2) return 0;

    let gcd = 0;

    for (i = Math.min(n1, n2); i >= 0; i--) {
        if (n1 % i == 0 && n2 % i == 0) {
            return i;
        }
    }
}


console.log("gcdOptimze", gcdOptimze(20, 40))


// function lcdNumber(n1, n2) {
//     if (!n1 || !n2) return 0;

//     let i = 1;

//     while (i <= Math.min(n1, n2)) {
//         if (n1 % i == 0 && n2 % i == 0) {
//             return i
//         }

//         i++;
//     }
// }

// console.log("LCD", lcdNumber(10, 20))

// // console.log("gcd of 20 40", gcdNumber(20, 40))


/**
 * Compute the greatest common divisor (GCD) of `a` and `b` using the
 * Euclidean algorithm (remainder-based).
 *
 * If either `a` or `b` is falsy the function returns `0`.
 * The algorithm repeatedly replaces the larger number with its remainder
 * when divided by the smaller number until one of them becomes zero; the
 * non-zero value is the GCD.
 *
 * @param {number} a - First positive integer.
 * @param {number} b - Second positive integer.
 * @returns {number} The greatest common divisor of `a` and `b`.
 * @example
 * // returns 20
 * gcdEuclidean(20, 40);
 */
function gcdEuclidean(a, b) {
    if (!a || !b) return 0;


    while (a > 0 && b > 0) {


        if (a > b) {
            a = a % b;
        } else {
            b = b % a;
        }
    }

    if (a == 0) {
        return b
    } else {
        return a;
    }
} 

console.log("gcdEuclidean", gcdEuclidean(20, 40))