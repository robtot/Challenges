const mockfs = require('mock-fs');
const hd = require('../hidden_digits.js');
var assert = require('assert');

function captureStream(stream){
  var oldWrite = stream.write;
  var buf = '';
  stream.write = function(chunk, encoding, callback){
    buf += chunk.toString(); // chunk is a String or Buffer
    oldWrite.apply(stream, arguments);
  }

  return {
    unhook: function unhook(){
     stream.write = oldWrite;
    },
    captured: function(){
      return buf;
    }
  };
}

describe('getLines Test Suite: ', () => {
  //Hooks
  before(() => {
    mockfs({
      'test_single_line_input.txt': 'hello world!',
      'test_input.txt': "abcdefghik\nXa,}A#5N}{xOBwYBHIlH,#W\n(ABW>'yy^'M{X-K}q,\n6240488"
    });

  });

  after(() => {
    mockfs.restore();
  });

  //Test Cases
  describe('Using nonexistent file for getLines', () => {
    it('should throw Error with File Not Found message', () => {
      assert.throws(() => { hd.getLines('nosuchfile29493405.txt') }, Error, /File Not Found:/);
    });
    
  });

  describe('Using numerical input for getLines', () => {
    it('should throw TypeError', () => {
      assert.throws(() => { hd.getLines(6347253) }, TypeError);
    });

  });

  describe('Using valid file with single line for getLines', () => {
    it('should return valid list with one line', () => {
      assert.deepEqual(hd.getLines('test_single_line_input.txt'), ['hello world!']);
    });

  });

  describe('Using valid file input for getLines', () => {
    it('should return valid line list', () => {
      assert.deepEqual(hd.getLines('test_input.txt'), ["abcdefghik", "Xa,}A#5N}{xOBwYBHIlH,#W", "(ABW>'yy^'M{X-K}q,", "6240488"]);
    });

  });

});

describe('getHiddenDigits Test Suite: ', () => {
  //Test Cases
  describe('Input "abcdefghijk"', () => {
    it('should return 0123456789', () => {
      assert.equal(hd.getHiddenDigits("abcdefghijk"), "0123456789");
    });

  });

  describe('Input "Xa,}A#5N}{xOBwYBHIlH,#W"', () => {
    it('should return 05', () => {
      assert.equal(hd.getHiddenDigits("Xa,}A#5N}{xOBwYBHIlH,#W"), "05");
    });

  });

  describe("Input \"(ABW>'yy^'M{X-K}q,\"", () => {
    it('should return "NONE"', () => {
      assert.equal(hd.getHiddenDigits("(ABW>'yy^'M{X-K}q,"), "NONE");
    });

  });

  describe('Input "6240488"', () => {
    it('should return 6240488', () => {
      assert.equal(hd.getHiddenDigits("6240488"), "6240488");
    });

  });

  describe('Input integer type', () => {
    it('should return TypeError', () => {
      assert.throws(() => { hd.getHiddenDigits(6347253) }, TypeError);
    });

  });

  describe('Input ""', () => {
    it('should return "NONE"', () => {
      assert.equal(hd.getHiddenDigits(""), "NONE");
    });

  });

});

describe('main Test Suite: ', () => {
  //Hooks
  before(() => {
    // mock files
    mockfs({
      'test_input.txt': "abcdefghik\nXa,}A#5N}{xOBwYBHIlH,#W\n(ABW>'yy^'M{X-K}q,\n6240488",
      'empty_file.txt': ""
    });

    //store original process.argv so mocked process.argv can revert to it after
    this.originalArgv = process.argv;
  });

  after(() => {
    mockfs.restore();
    Object.defineProperty(process, 'argv', {
      value: this.originalArgv
    });

  });

  //Hook for capturing stdout
  var stdout_hook;

  beforeEach(function(){
    stdout_hook = captureStream(process.stdout);
  });

  afterEach(function(){
    stdout_hook.unhook(); 
  });

  //Test Cases
  describe('main method basic test', () => {
    it('should print valid response to console.log', () => {
      Object.defineProperty(process, 'argv', {
        value: ["node", "mock_hidden_digits.test.js", "test_input.txt"]
      });

      hd.main();
      assert.equal(stdout_hook.captured(), "012345678\n05\nNONE\n6240488\n");
    });

  });

  describe('main method empty file test', () => {
    it('should print NONE to console.log', () => {
      Object.defineProperty(process, 'argv', {
        value: ["node", "mock_hidden_digits.test.js", "empty_file.txt"]
      });
      
      hd.main();
      assert.equal(stdout_hook.captured(), "NONE\n");
    });

  });

  describe('main method no file test', () => {
    it('should print NONE to console.log', () => {
      Object.defineProperty(process, 'argv', {
        value: ["node", "mock_hidden_digits.test.js", "nonexistenfile1035939104.txt"]
      });
      
      assert.throws(() => { hd.main() }, Error, /File Not Found:/);
    });

  });

  describe('main method missing command line arguments', () => {
    it('should print should print missing command line message and end', () => {
      Object.defineProperty(process, 'argv', {
        value: ["node",   "mock_hidden_digits.test.js"]
      });
      
      hd.main();
      assert.equal(stdout_hook.captured(), "Missing filename command line parameter! Correct usage: 'hidden_digits.js <filename>'\n");
    });

  });

});