var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {
  if (line !== '') {
    var num = Number('0x' + line);
    process.stdout.write(num + '\n');
  }

});
