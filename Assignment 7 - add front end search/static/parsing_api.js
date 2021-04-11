
function get_input(){
  let inputVal = document.getElementById("input_text").value;
  console.log(inputVal);

  
  let request = new XMLHttpRequest();
  let url = 'http://127.0.0.1:3000/api/users';
  let final_url = url + "?username="+inputVal;
  console.log(final_url);

  request.open('GET', final_url, true);

  request.onload = function(){
    if (this.status >= 200 && this.status < 400) {
      let data = JSON.parse(this.response);
      data = data["data"];
      let out_div = document.getElementById("search_account");

      document.getElementById("click_to_search").addEventListener("click", function(){
        let output_name = data["name"];
        let final = output_name + " (" + inputVal + ")";      
        let content = document.createTextNode(final);
        out_div.removeChild(out_div.firstChild);
        out_div.appendChild(content);        
      })
    }
  }
  request.send();
}









// request.onload = function(){
//   if (this.status >= 200 && this.status < 400) {
//     document.getElementById("click_to_search").addEventListener("click", function(){

//       
//       console.log(inputVal);
//       let final_url = url + "?username="+inputVal;
//       console.log(final_url);
//       request.open('GET', final_url, true);

//       let data = JSON.parse(this.response);
//       data = data["data"];

//       let out_div = document.getElementById("search_account");
//       let output_name = data[i]["name"];
//       let final = output_name + " (" + inputVal + ")";      
//       let content = document.createTextNode(final);
//       out_div.removeChild(out_div.firstChild);
//       out_div.appendChild(content);
//     })
//   }
//   request.send();
// }




















// let request = new XMLHttpRequest();
// let url = 'http://127.0.0.1:3000/api/users';
// request.open('GET', url, true);


// document.getElementById("click_to_search").addEventListener("click", function(){
//   let searchinputVal = 'ply';
//   // let searchinputVal = document.getElementById("input_text").value;
//   console.log(searchinputVal);

//   let final_url = url+"?username="+searchinputVal;

//   request.open('GET', final_url, true);
  

//   let out_div = document.getElementById("search_account");  

//   request.onload = function(){
//     if (this.status >= 200 && this.status < 400) {
//       let data = JSON.parse(this.response);
//       data = data["data"];
//       console.log(data["username"]);
//       let output_name = data["name"];

//       let final = output_name + " (" + data["username"] + ")";
//       let content = document.createTextNode(final);
      
//       // since if don't clear will keep appending output
//       out_div.removeChild(out_div.firstChild); 
//       out_div.appendChild(content);    
//     }
//   }
//   request.send();
// })








  



// request.onload = function(){
//   if (this.status >= 200 && this.status < 400) {
//     let data = JSON.parse(this.response);
//     data = data["data"];
//     console.log(data);
//     console.log(data[0]);
    
//     document.getElementById("click_to_search").addEventListener("click", function(){
//       let inputVal = document.getElementById("input_text").value;
//       console.log(inputVal);

//       let url = 'http://127.0.0.1:3000/api/users?username='+inputVal;
//       request.open('GET', url, true);



//       let out_div = document.getElementById("search_account");
//       for (let i=0; i<data.length;i++){
//         if (data[i]["username"]==inputVal){
//           let output_name = data[i]["name"];
//           let final = output_name + " (" + inputVal + ")";
//           console.log(final);
          
//           let content = document.createTextNode(final);
//           out_div.appendChild(content);
//         }else {
//           console.log("error");
//         }
//       } 
//     })
//   }
// }





function get_name2(){
  let inputVal = document.getElementById("input_text").value;
  console.log(inputVal);
}


