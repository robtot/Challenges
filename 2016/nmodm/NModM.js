var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {
  if (line !== '') {
    var nums = line.split(',');
    var n = parseInt(nums[0]);
    var m = parseInt(nums[1]);
    while (n - m >= 0) {
      n = n - m;
    }

    process.stdout.write(n + '\n');
  }

});
