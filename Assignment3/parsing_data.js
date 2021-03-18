// http://youmightnotneedjquery.com/
// https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Traversing_an_HTML_table_with_JavaScript_and_DOM_Interfaces


let request = new XMLHttpRequest();
request.open('GET', 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json', true);

request.onload = function() {
  if (this.status >= 200 && this.status < 400) {
    let data = JSON.parse(this.response);
    data = data["result"]["results"];

    let tbl = document.querySelector("table");

    // create table with 2*4 format
    for (let i=0; i<2; i++){
      let row = document.createElement("tr");
      for (let j=0; j<4; j++){
        let cell = document.createElement("td");

        // image
        let image = document.createElement("img");
        image.src = data[4*i+j].file.split("jpg")[0]+"jpg"
        image.className = "img-size";

        // image title
        let title = document.createElement("div");
        title.className = "img-title";
        let cellText = document.createTextNode(data[4*i+j].stitle);
        title.appendChild(cellText);

        cell.appendChild(image);
        cell.appendChild(title);
        row.appendChild(cell);
      }
      tbl.appendChild(row);
    }
  } 
};

request.send();