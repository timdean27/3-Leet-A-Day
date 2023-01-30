function gameWinner(colors) {

  let Wcount = 0;
  let Bcount = 0;
  for (let i = 0; i < colors.length; i++) {
    if (colors[i] == "w" && colors[i + 1] == "w" && colors[i - 1] == "w") {
      // console.log(i)
      Wcount++;
      //  console.log("Wcount",Wcount)
    }
    if (colors[i] == "b" && colors[i + 1] == "b" && colors[i - 1] == "b") {
      // console.log(i)
      Bcount++;
      //  console.log("Bcount",Bcount)
    }
  }
  if (Wcount > Bcount) {
    console.log("Wendy");
    return true;
  } else {
    console.log("Bob");
    return false;
  }
}

console.log(gameWinner("wbwwwwwbb"));
console.log(gameWinner("ww"));
console.log(gameWinner("wwbb"));
console.log(gameWinner("wwwbbbbwww"));
console.log(gameWinner("wwwwwbbbbbbwwwww"));
