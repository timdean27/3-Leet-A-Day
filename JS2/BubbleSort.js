
function bubbleSort(arr) {
    const n = arr.length;

    for (let i = 0; i < n - 1; i++) {
        // Last i elements are already sorted, so we don't need to check them again
        for (let j = 0; j < n - i - 1; j++) {
            // Swap if the element found is greater than the next element
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j + 1]
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    return arr;
}

let numbers = [4, 2, 7, 1, 9];
bubbleSort(numbers);
console.log(numbers); // Output: [1, 2, 4, 7, 9]
