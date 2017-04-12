//CodeEval Hidden Digits Challenge Solution

function getLines(filename) {
	var fs = require('fs');
	try {
		var lines = fs.readFileSync(filename).toString().split('\n');
	} catch (err) {
		if (err.code === 'ENOENT') {
			throw new Error('File Not Found: ' + filename);
		} else {
			if (typeof filename !== "string") {
				throw new TypeError('Expecting string as input, instead received ' + typeof filename);
			}

			throw err;
		}

	}

	return lines;
}

function getHiddenDigits(line) {
	if (typeof line !== 'string') {
		throw new TypeError('getHiddenDigits expecting string as input! Instead received ' + typeof line);
	}

	var hidden_chars = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9};
	var result = '';
	var noneFound = true;
	for (var i = 0, len = line.length; i < len; i++) {
		if (!isNaN(line[i]) && line[i] != '' && line[i] != ' ') {
			result += line[i];
			noneFound = false;
		} else if (line[i].match(/[a-j]/)) {
			result += hidden_chars[line[i]];
			noneFound = false;
		}

	}

	if (noneFound) {
		return 'NONE';
	} else {
		return result;
	}

}

function main() {
	if (process.argv.length < 3) {
		console.log("Missing filename command line parameter! Correct usage: 'hidden_digits.js <filename>'");
		return 0;
	} 

	var filename = process.argv[2];
	var lines = getLines(filename);
	lines.forEach(function(line) {
		console.log(getHiddenDigits(line));
	});

}

if (require.main === module) {
    main();
}

module.exports = {
	getLines, getHiddenDigits, main
};