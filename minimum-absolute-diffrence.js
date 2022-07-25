var minimumAbsDifference = function(integers) {
    integers.sort((a, b) => a - b);
    let result = [],
    min = 999999

for (let i = 0; i < integers.length - 1; i++) {
    let diff = integers[i + 1] - integers[i]
    if (diff < minNum) {
        result = [[integers[i], integers[i + 1]]]
        minNum = diff
    } else if (diff === minNum) {
        result.push(integers[i], integers[i + 1])
    }
}
return result
};
console.log(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))