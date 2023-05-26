// Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

// For the purpose of this exercise, you should also capitalize connecting words like "the" and "of".

// Remember to use Read-Search-Ask if you get stuck. Write your own code.

// Here are some helpful links:

// String.prototype.split()

function titleCase(str) {
    var newString = '';
    var firstLetter = '';
    var restOfString = '';
    var split = str.split(' ');
    var space = ' ';
    for (var i = 0; i < split.length; i++) {
        firstLetter = split[i].charAt(0).toUpperCase();
        restOfString = split[i].toLowerCase().slice(1);
        if (i == split.length-1) {
          space = '';
        }
        newString += firstLetter + restOfString + space;
  }
  return newString;
}

titleCase("I'm a little tea pot");

// titleCase("I'm a little tea pot") should return a string.
// titleCase("I'm a little tea pot") should return "I'm A Little Tea Pot".
// titleCase("sHoRt AnD sToUt") should return "Short And Stout".
// titleCase("HERE IS MY HANDLE HERE IS MY SPOUT") should return "Here Is My Handle Here Is My Spout".