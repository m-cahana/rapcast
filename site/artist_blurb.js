//Requirements
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

var context = require("./../output/search_data.json");

 function build() {
   for var i

 }
