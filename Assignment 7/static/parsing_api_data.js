

let request = new XMLHttpRequest();
request.open('GET', 'http://127.0.0.1:3000/api/users', true);
// request.open('GET', 'http://127.0.0.1:5000/api/users', true);



request.onload = function(){
  if (this.status >= 200 && this.status < 400) {
    let data = JSON.parse(this.response);
    data = data["data"];
    
    document.getElementById("click_to_search").addEventListener("click", function(){
      let inputVal = document.getElementById("input_text").value;
      console.log(inputVal);

      let out_div = document.getElementById("search_account");
      for (let i=0; i<data.length;i++){
        if (data[i]["username"]==inputVal){
          let output_name = data[i]["name"];
          let final = output_name + " (" + inputVal + ")";
          console.log(final);
          
          let content = document.createTextNode(final);
          out_div.appendChild(content);
        }else {
          console.log("error");
        }
      } 
    })
  }
}

request.send();



function get_name2(){
  let inputVal = document.getElementById("input_text").value;
  console.log(inputVal);
}


