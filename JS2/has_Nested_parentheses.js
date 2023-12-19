// # Write a function that reverses characters in (possibly nested) parentheses in the input string.

// # Input strings will always be well-formed with matching ()s.

// # Example

// # For inputString = "(bar)", the output should be
// # solution(inputString) = "rab";
// # For inputString = "foo(bar)baz", the output should be
// # solution(inputString) = "foorabbaz";
// # For inputString = "foo(bar)baz(blim)", the output should be
// # solution(inputString) = "foorabbazmilb";
// # For inputString = "foo(bar(baz))blim", the output should be
// # solution(inputString) = "foobazrabblim".
// # Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".



function solution(inputString){

    function reverseString(sub_string){
        return sub_string.split('').reverse().join('');
    }


    let hasNestedParentheses = true;

    while (hasNestedParentheses) {
        let parStart = 0;
        let parEnd = 0;
        hasNestedParentheses = false;

        for (let i = 0; i < inputString.length; i++) {
            if (inputString[i] === '(') {
                parStart = i;
            } else if (inputString[i] === ')') {
                parEnd = i;
                let nestedString = inputString.substring(parStart + 1, parEnd); // Extract the string inside parentheses
                let reversedNestedString = reverseString(nestedString);
                inputString = inputString.substring(0, parStart) + reversedNestedString + inputString.substring(parEnd + 1);
                hasNestedParentheses = true; // Set the flag to true to indicate nested parentheses were found
                break; // Break the loop after processing one pair of parentheses
            }
        }
    }
}