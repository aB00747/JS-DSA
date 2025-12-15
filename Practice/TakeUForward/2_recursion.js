
/**
 * Recursively prints numbers from 1 through 10 (inclusive).
 *
 * Uses a parameter `i` with default `1` to avoid a global counter.
 * The function does not return a value; it only prints to the console.
 *
 * @param {number} [i=1] - Current number to print.
 */
/**
 * Recursively prints numbers from the current value `i` up to 10 (inclusive).
 * Uses a default start value of `1` so the function can be called without arguments.
 *
 * @param {number} [i=1] - Current number to print; recursion advances by `i + 1`.
 * @returns {void}
 */
function print10(i = 1) {
    console.log("n ->", i);

    if (i >= 10) return;
    print10(i + 1);
}

// print10();


/**
 * Recursively computes the sum of integers from 1 through `i` using an accumulator.
 * This is implemented in a tail-recursive style: `sum` accumulates the running total.
 *
 * Example: `print_sum(3, 0)` computes 1 + 2 + 3 = 6 and returns 6.
 *
 * @param {number} i - Current index to add; recursion continues while `i >= 1`.
 * @param {number} sum - Accumulated sum so far (pass `0` to start).
 * @returns {number} The total sum from 1..original i (or the provided accumulator when `i < 1`).
 */
function print_sum(i, sum) {

    if (i < 1) {
        console.log("sum", sum);
        return sum;
    }

    return print_sum(i - 1, sum + i);
}

console.log(print_sum(3, 0));


/**
 * Computes the factorial of a non-negative integer `n` (n!).
 * Uses the standard recursive definition: 0! = 1, n! = n * (n-1)! for n > 0.
 *
 * @param {number} n - Non-negative integer whose factorial is to be computed.
 * @returns {number} Factorial of `n`.
 */
function factorial(n) {

    if (n == 0) {
        return 1;
    }

    return n * factorial(n - 1);
}

// console.log(factorial(3))




/**
 * Recursively computes the sum of integers from 1 through `n`.
 *
 * @param {number} n - Non-negative integer.
 * @returns {number} Sum of integers from 1..n (returns 0 when n is 0).
 */
function sumFunction(n) {

    if (n == 0) {
        return 0;
    }

    return n + sumFunction(n - 1);
}


console.log("sumFunction", sumFunction(3));

// swapping with two pointer recusion
/**
 * Reverse an array in-place using two-pointer recursion.
 * Swaps elements at indices `l` and `r`, then recurses inward until pointers meet.
 *
 * @template T
 * @param {number} l - Left index (start position).
 * @param {number} r - Right index (end position).
 * @param {T[]} arr - Array to reverse in-place.
 * @returns {T[]} The same array instance, reversed in-place.
 */
function swapFunc(l, r, arr) {
    if (l >= r) {
        return arr;
    }

    swapeArr(arr, l, r);
    // let tmp = arr[l];
    // arr[l] = arr[r];
    // arr[r] = tmp

    return swapFunc(l + 1, r - 1, arr);

}

/**
 * Swap two elements in an array at indices `l` and `r`.
 *
 * @template T
 * @param {T[]} arr - The array containing elements to swap.
 * @param {number} l - Index of the first element.
 * @param {number} r - Index of the second element.
 * @returns {T[]} The same array after the swap.
 */
function swapeArr(arr, l, r) {
    let tmp = arr[l];
    arr[l] = arr[r];
    arr[r] = tmp;

    return arr;
}

console.log("swapFunc", swapFunc(0, 4, [1, 3, 2, 5, 4]))



/**
 * Reverse an array by swapping one pair per recursive call.
 * This version accepts an index `i` (default 0) and swaps `arr[i]` with its
 * partner `arr[arr.length-1-i]`, then recurses with `i+1`.
 *
 * @template T
 * @param {T[]} arr - Array to reverse in-place.
 * @param {number} [i=0] - Current left index to swap; defaults to 0.
 * @returns {T[]} The same array instance, reversed in-place.
 */
function swapeOnePnt(arr, i = 0) {

    // base case: processed half the array (pointers crossed)
    if (i >= Math.floor(arr.length / 2)) {
        return arr;
    }

    const j = arr.length - 1 - i; // partner index from the right
    let tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;

    return swapeOnePnt(arr, i + 1);
}

console.log(swapeOnePnt([1, 3, 2, 5, 4], 0));


/**
 * Recursively checks whether a string is a palindrome.
 * Compares characters at indices `i` and `len - i - 1` and recurses inward.
 * Note: this function does not perform case-folding or remove non-alphanumeric
 * characters; it compares characters as-is.
 *
 * @param {string} str - The string to check (compared as provided).
 * @param {number} [i=0] - Current index for recursion (should be omitted by callers).
 * @returns {boolean} `true` if `str` is a palindrome, otherwise `false`.
 */
function isPaldirome(str, i = 0) {
    const len = str.length;
    if (i >= Math.floor(str.length / 2)) {
        return true;
    }

    if (str[i] != str[len - i - 1]) {
        return false;
    }

    return isPaldirome(str, i + 1);
}

console.log("isPaldirome", isPaldirome("MADAM", 0));


// Multi - Recursion
// (F_{0}=0) (F_{1}=1) (F_{2}=0+1=1) (F_{3}=1+1=2) (F_{4}=1+2=3)

/**
 * Recursively computes the nth Fibonacci number.
 * Uses the simple recursive definition: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
 * This implementation has exponential time complexity and is intended for
 * demonstration or small `n` only.
 *
 * @param {number} n - Non-negative integer index in the Fibonacci sequence.
 * @returns {number} The nth Fibonacci number.
 */
function fibonaci(n) {
    if (n <= 1) {
        return n;
    }

    return fibonaci(n - 1) + fibonaci(n - 2);
}

console.log("fibonaci", fibonaci(4));