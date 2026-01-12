function maxFrequencyElements(nums) {
    const freq = {};
    for (const num of nums) {
        freq[num] = (freq[num] || 0) + 1;
    }

    const counts = Object.values(freq);
    if (counts.length === 0) return 0;

    const max_freq = Math.max(...counts);

    let total = 0;
    for (const count of counts) {
        if (count === max_freq) total += count;
    }

    return total;
}

console.log(maxFrequencyElements([1, 2, 2, 3, 1, 4, 2]));