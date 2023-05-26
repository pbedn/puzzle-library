// Write a function which takes a ROT13 encoded string as input and returns a decoded string.

// All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), but do pass them on.

// Remember to use Read-Search-Ask if you get stuck. Try to pair program. Write your own code.

// Here are some helpful links:

// String.prototype.charCodeAt()
// String.fromCharCode()

var start = 'A'.charCodeAt();
var end = 'Z'.charCodeAt();

function rot13(str) {
  var newString = "";
  for (var i=0; i<str.length; i++){
    var code = str[i].charCodeAt();
    if (code >= start) {
      code = code + 13;
      if (code > end) {
        code = code - 26;
      }
    }
    newString += String.fromCharCode(code);
  }
  return newString;
}

// Change the inputs below to test
rot13("SERR PBQR PNZC");

rot13("SERR PBQR PNZC") should decode to "FREE CODE CAMP"
rot13("SERR CVMMN!") should decode to "FREE PIZZA!"
rot13("SERR YBIR?") should decode to "FREE LOVE?"
rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.") should decode to "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."