// Repeat a given string (first argument) num times (second argument). Return an empty string if num is not a positive number.

// Remember to use Read-Search-Ask if you get stuck. Write your own code.

// Here are some helpful links:

// Global String Object

function repeatStringNumTimes(str, num) {
  // repeat after me
  if (num < 0) return '';

//   return str * num;
  return num ? Array(num + 1).join(str) : "";
}

repeatStringNumTimes("abc", 3);

repeatStringNumTimes("*", 3) should return "***".
repeatStringNumTimes("abc", 3) should return "abcabcabc".
repeatStringNumTimes("abc", 4) should return "abcabcabcabc".
repeatStringNumTimes("abc", 1) should return "abc".
repeatStringNumTimes("*", 8) should return "********".
repeatStringNumTimes("abc", -2) should return "".