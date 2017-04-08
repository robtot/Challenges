var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {
  line = line.trim();
  if (line.length < 1) { return 0; }
  var menu = JSON.parse(line);
  var sum = 0;
  for (var i in menu.menu.items) {
    var item = menu.menu.items[i];
    if (item !== null && item.hasOwnProperty('label')) {
      sum += item.id;

    }

  }

  console.log(sum);
});
