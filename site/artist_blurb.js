//Requirements
var _ = require('lodash');
var Handlebars = require('handlebars');
var fs = require('fs');
var mkdirp = require('mkdirp');
var prettifyHtml = require('prettify-html');

// Template for artists' divs
var artistHTML =
  "div id='test'>" +
    "<h3>{{artist_name}}</h3>" +
    "<h4>{{city}}</h4>" +
    "<p>City Unigrams: {{city_unigrams}}</p>" +
    "<p>City Bigrams: {{city_bigrams}}</p>" +
    "<p>Most common words: {{common_words}}</p>" +
  "</div>"

var eek = require('./templates/artist.hbs');
var context = require("./../output/search_data.json");

var artists = [];
for (var artist in context) artists.push(artist);
// console.log(artists)

 function blurbBuild() {
   for (var i = 0; i < artists.length; i++) {
     var fileName = './dist/'+artists[i]+'.html';
     var stream = fs.createWriteStream(fileName);
     var result = eek(context[artists[i]]);
     stream.write(result);
     stream.end()
   }
 }

function pageBuild() {
  var artistDivs = './outtie.html';
  var dropdown = './dropdown.html';
  var artistStream = fs.createWriteStream(artistDivs);
  var dropdownStream = fs.createWriteStream(dropdown);
  for (var i = 0; i < artists.length; i++) {
    var artistResult = eek(context[artists[i]]);
    artistStream.write(artistResult);
    dropdownStream.write("<li>" + artists[i] + "</li>");
  }
  artistStream.end()
  dropdownStream.end()
}

 // blurbBuild()
 pageBuild()
