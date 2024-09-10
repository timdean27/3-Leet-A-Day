// Given an array of strings words and an integer k, return the k most frequent strings.

// Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

// Example 1:

// Input: words = ["i","love","leetcode","i","love","coding"], k = 2
// Output: ["i","love"]
// Explanation: "i" and "love" are the two most frequent words.
// Note that "i" comes before "love" due to a lower alphabetical order.
// Example 2:

// Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
// Output: ["the","is","sunny","day"]
// Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


var topKFrequent = function(words, k) {
//hash map for words
let hash ={}

for(let i = 0; i < words.length; i++){
    if (!words) return [];
    //if hash already exists push words[i] into key
    if(hash[words[i]]){
        hash[words[i]]++
    }
    //else if hash does not exist set hash name with words[i] = to words[i]
    else{
        hash[words[i]] = 1
    }
}
console.log(hash)
let result = Object.keys(hash).sort((a,b)=>{
    let countCompare = hash[b] - hash[a];
    if (countCompare == 0) return a.localeCompare(b);
    else return countCompare;
}   
);
return result.slice(0, k);
};

console.log(topKFrequent(["i","love","leetcode","i","love","coding"],1))
console.log(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"] , 4))