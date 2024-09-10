function product(a,b) {
  var prd = a,i = a;
 
  while (i++< b) {
    prd*=i;
  }
  return prd;
}


function combinations(n, r) 
{
  if (n==r || r==0) 
  {
    return 1;
  } 
  else 
  {
    r=(r < n-r) ? n-r : r;
    return product(r+1, n)/product(1,n-r);
  }
}


console.log(combinations(6, 2));
console.log(combinations(5, 3));