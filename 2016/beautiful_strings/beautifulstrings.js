var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {
  var occurences = Array.apply(null, Array(26)).map(Number.prototype.valueOf, 0);
  for (var i = 0; i < line.length; i++) {
    var c = line.charAt(i);
    switch (c) {
      case 'A': case 'a':
        occurences[0] += occurences[0] + 1;
        break;
      case 'B': case 'b':
        occurences[1] += occurences[1] + 1;
        break;
      case 'C': case 'c':
        occurences[2] += occurences[2] + 1;
        break;
      case 'D': case 'd':
        occurences[3] += occurences[3] + 1;
        break;
      case 'E': case 'e':
        occurences[4] += occurences[4] + 1;
        break;
      case 'F': case 'f':
        occurences[5] += occurences[5] + 1;
        break;
      case 'G': case 'g':
        occurences[6] += occurences[6] + 1;
        break;
      case 'H': case 'h':
        occurences[7] += occurences[7] + 1;
        break;
      case 'I': case 'i':
        occurences[8] += occurences[8] + 1;
        break;
      case 'J': case 'j':
        occurences[9] += occurences[9] + 1;
        break;
      case 'K': case 'k':
        occurences[10] += occurences[10] + 1;
        break;
      case 'L': case 'l':
        occurences[11] += occurences[11] + 1;
        break;
      case 'M': case 'm':
        occurences[12] += occurences[12] + 1;
        break;
      case 'N': case 'n':
        occurences[13] += occurences[13] + 1;
        break;
      case 'O': case 'o':
        occurences[14] += occurences[14] + 1;
        break;
      case 'P': case 'p':
        occurences[15] += occurences[15] + 1;
        break;
      case 'Q': case 'q':
        occurences[16] += occurences[16] + 1;
        break;
      case 'R': case 'r':
        occurences[17] += occurences[17] + 1;
        break;
      case 'S': case 's':
        occurences[18] += occurences[18] + 1;
        break;
      case 'T': case 't':
        occurences[19] += occurences[19] + 1;
        break;
      case 'U': case 'u':
        occurences[20] += occurences[20] + 1;
        break;
      case 'V': case 'v':
        occurences[21] += occurences[21] + 1;
        break;
      case 'W': case 'w':
        occurences[22] += occurences[22] + 1;
        break;
      case 'X': case 'x':
        occurences[23] += occurences[23] + 1;
        break;
      case 'Y': case 'y':
        occurences[24] += occurences[24] + 1;
        break;
      case 'Z': case 'z':
        occurences[25] += occurences[25] + 1;
        break;
    }
  }

  console.log(occurences.toString());
});
