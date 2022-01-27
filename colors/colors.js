/* 
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 * 
 * This is a Color class for converting between HEX and RGB/A values
 * relatively quickly and easily.
 */
class Color {
		constructor(red,green,blue,alpha){
			  this.red = (red===undefined)?255:red;
			  this.green = (green===undefined)?255:green;
			  this.blue = (blue===undefined)?255:blue;
			  this.alpha = (alpha===undefined)?1:alpha;
			  }
	  get rgba(){
		    	return (this.red, this.green, this.blue, this.alpha);
		    }
	  get hex(){
		      return (this.red | 1 << 8).toString(16).slice(1) +
			        (this.green | 1 << 8).toString(16).slice(1) +
			        (this.blue | 1 << 8).toString(16).slice(1);
		    }
	// Warning: does not return proper alpha value
	  get hex8(){
		      return (this.red | 1 << 8).toString(16).slice(1) +
			      (this.green | 1 << 8).toString(16).slice(1) +
			      (this.blue | 1 << 8).toString(16).slice(1) + 
			      (255*this.alpha | 1 << 8).toString(16).slice(1);
		    }
	  *from_rgba_string(string){
		      (this.red, this.green, this.blue, this.alpha) = string.match(/rgba?\(\s?((25[0-5]|2[0-4]\d|1\d{1,2}|\d\d?)\s*,\s*?){2}(25[0-5]|2[0-4]\d|1\d{1,2}|\d\d?)\s*,?\s*([01]\.?\d*?)?\)/);
		    }

	   *from_hex_string(string){
			return "Not implemented";
	   }
}

function test(string, hex){
	    var color = new Color;
	    color.from_rgba_string(string);
	    console.log(color.hex, hex);
}

test('rgb(255,255,255)','ffffff');
