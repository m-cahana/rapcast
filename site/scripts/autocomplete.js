var artists = ['Dana Dane', 'Eric B. & Rakim', 'A Boogie Wit Da Hoodie', 'Beanie Sigel', 'Killer Mike', 'Oj Da Juiceman', 'A$Ap Ferg', 'Az ', 'Tha Alkaholiks', 'Towkio', 'Mack 10', 'Epmd', 'Dmx', 'Big Tymers', 'The D.O.C.', 'Boogie Down Productions', 'Method Man', 'B.G.', 'Nicki Minaj', 'Young Thug', 'Pras Michel', 'Common ', 'Juicy J', 'Lil Uzi Vert', 'Kyle', 'Madeintyo', 'Flo Rida', 'Lloyd Banks', 'G-Eazy', 'De La Soul', 'Yg', 'Styles P', 'Eminem', 'Mc Eiht', 'O.C.', 'Lil Kim', 'Lil Dicky', 'Slum Village', 'Bow Wow', 'Hoodie Allen', 'Eazy-E', 'Slick Rick', 'Lil Yachty', 'Yung Joc', 'Machine Gun Kelly', "Cam'Ron", 'Juelz Santana', 'House Of Pain', 'Silkk The Shocker', "Lil' Flip", 'Kirko Bangz', 'Big L', 'Rick Ross', 'Chief Keef', 'N.W.A', 'N.O.R.E.', 'Kool G Rap', 'Mia X', 'Public Enemy', 'Nappy Roots', 'Memphis Bleek', 'Young Gunz', 'P. Diddy', 'Big Pun ', 'Mc Lyte', 'Jadakiss', 'Talib Kweli', 'Mistah F.A.B.', 'Ilovemakonnen', 'The Game', 'Nipsey Hussle', 'Erick Sermon', 'Afroman', 'Q-Tip', 'Dej Loaf', 'Desiigner', 'Lil Wayne', 'D.R.A.M.', 'Keith Murray', 'Young Mc', 'Busta Rhymes', 'Kanye West', 'Lords Of The Underground', '50 Cent', 'Fabolous', 'Big K.R.I.T.', 'B.O.B', 'Mos Def', 'Coolio ', 'Lil Durk', 'Missy Elliot', 'Chamillionaire', "Royce Da 5'9", 'Trick Daddy', 'Tyga', 'Bubba Sparxxx', 'Fugees', 'Outkast', 'Dj Jazzy Jeff & The Fresh Prince', 'Project Pat', 'O.T. Genasis', 'Nelly', 'J. Cole', 'Que', 'Lil Jon', 'Young M.A.', 'Travis Porter', 'Tech N9Ne', 'Sir Mix-A-Lot', 'Fetty Wap', 'Travis Scott', 'Yelawolf', 'Tha Dogg Pound', 'Chubb Rock', 'Bankroll Fresh', 'Danny Brown', 'Goodie Mob', 'Brand Nubian', 'Three 6 Mafia', 'Jay Rock', 'Snoop Dogg ', 'Ca$H Out', 'Russ', 'Soulja Slim', 'Arrested Development', 'Skeme', 'Lupe Fiasco', 'Action Bronson', 'Ugk', 'Freeway', 'Juvenile', 'Earl Sweatshirt', 'Og Maco', 'Slim Thug', 'Webbie', 'Wiz Khalifa', 'Raekwon', 'Petey Pablo', 'French Montana', 'Scarface', 'Iggy Azalea', 'Maino', 'A Tribe Called Quest', 'Kid Ink', 'Chevy Woods', 'Krayzie Bone', 'Ace Hood', 'Redman', 'D12', 'The Notorious B.I.G.', 'The Alchemist', 'Bone Thugs-N-Harmony', 'Too $Hort', 'T.I.', 'Kodak Black', 'Ugly God', 'Hopsin', 'Lil Bibby', 'Jim Jones', 'Shy Glizzy', 'Shawty Lo', 'David Banner', 'Kendrick Lamar', 'Canibus', 'Black Rob', 'Young Dolph', 'Ma$E', 'Ja Rule', 'Krs-One', 'The Lox', 'Tinie Tempah', 'Post Malone', 'Warren G', 'Meek Mill', 'Childish Gambino', 'Monty', 'Ying Yang Twins', 'Kurtis Blow', 'Pusha T', 'Dreezy', 'Wyclef Jean', 'The Beatnuts', '2Pac', 'Gang Starr', 'King Chip', 'E-40', 'Obie Trice', 'Mike Jones', 'Rza', 'Field Mob', 'Wu-Tang Clan ', 'Cappadonna', 'Ramy Ma', 'Dae Dae', 'Eve', '2 Chainz', 'Digital Underground', 'Macklemore & Ryan Lewis', 'Rocko', 'Cassidy', 'Nate Dogg', 'Dj Quik', 'Mystikal', 'Salt-N-Pepa', 'Problem', 'Mobb Deep', 'Kool Moe Dee', 'Ghostface Killah', 'Digable Planets', 'Das Efx', 'Wale', 'The Roots', 'Rae Sremmurd', 'Boosie Badazz', 'Ludacris', 'Clipse', 'Big Daddy Kane', 'Trinidad James', 'Lil Scrappy', 'Gza', 'Yo Gotti', 'T-Wayne', 'Iamsu!', 'Sage The Gemini', 'Ice Cube', 'Youngbloodz', 'The Pharcyde', 'Schoolboy Q', '3Rd Bass', 'Lost Boyz', 'Kardinal Offishall', 'Naughty By Nature', 'Luniz', 'Dilated Peoples', 'Vanilla Ice', 'Beastie Boys', 'Cypress Hill', 'Craig Mack', 'Ice-T', 'Nas', 'Waka Flocka Flame', 'Nav', 'Migos', 'Biz Markie', 'Curren$Y', 'Master P', 'Big Boi', 'Drake', 'Chingy', 'Gucci Mane', 'Tony Yayo', 'Bun B', 'Roscoe Dash', 'Dr. Dre', 'Young Buck', "Ol' Dirty Bastard", 'Tink', 'Xxxtentacion', 'Onyx', 'Xzibit', 'Ll Cool J ', 'Crime Mob', 'Mac Miller', 'Mc Hammer', 'Lauryn Hill', 'Kevin Gates', 'Gorilla Zoe', 'Plies', 'Kris Kross', 'Young Dro', 'Murphy Lee', 'Young Jeezy', 'Pastor Troy', 'Big Sean', 'Joey Bada$$', 'Doug E. Fresh', 'Soulja Boy', 'Pharoahe Monch', 'Birdman', 'Chance The Rapper', 'Future', 'Fat Joe', 'A$Ap Rocky', 'Logic', 'Rich Homie Quan', 'K Camp', 'Joe Budden', 'Da Brat', 'T-Pain', 'Yfn Lucci', 'Geto Boys', 'Cyhi The Prynce', 'Grand Puba', 'Black Sheep ', 'Young Chris', 'Shyne', 'Paul Wall', 'Jidenna', 'Lil Reese', 'Camp Lo', 'Twista', 'The 2 Live Crew', 'Run-Dmc', 'Jay-Z', 'Kid Cudi']


function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
              b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}

autocomplete(document.getElementById("myInput"), artists);

document.getElementById("artistinput").addEventListener("click", function(event){
    // document.getElementsByTagName("form").reset();
    var divsToHide = document.getElementsByClassName("artist_info");
    for (var i = 0; i < divsToHide.length; i++) {
        divsToHide[i].style.display = "none";
    }
    document.getElementById(document.getElementById("myInput").value).style = "display: show;";
});
