example
let p=new Promise((resolve, reject) => {
    const a=5
    if (a==3) {resolve
        
    } else {
        reject
    }
    
});
p.then((message)=>{console.log(message);
}).catch((message)=>{console.log(message);
} )
//callback example
function getMoneyBack(money, callback) {
    if (typeof money !== 'number') {
      callback(null, new Error('money is not a number'))
    } else {
      callback(money)
    }
  }
  
  const money = getMoneyBack(1200)
  console.log(money)
//promises
function getMoneyBack(money) {
    return new Promise((resolve, reject) => {
      if (typeof money !== 'number') {
        reject(new Error('money is not a number'))
      } else {
        resolve(money)
      }
    })
  }
  
  getMoneyBack(1200).then((money) => {
    console.log(money)
  }).catch((error)=>{console.log("error");
  }  )
example
const add = (num1, num2) => new Promise((resolve) => resolve(num1 + num2))

const multiply = (num1, num2) => new Promise((resolve) => resolve(num1 * num2))

const fail = (num1) =>
  new Promise((resolve, reject) =>
    setTimeout(() => reject(new Error('You, my friend, were too late')), 200),
  )
  
const fail2 = (num1) =>
  new Promise((resolve, reject) =>
    setTimeout(
      () => reject(new Error('Being late is never a good habit')),
      100,
    ),
  )
  
const promises = [add(2, 4), multiply(5, 5), fail('hi'), fail2('hello')]

Promise.allSettled(promises)
  .then((result) => {
    console.log(result)
  })
  .catch((error) => {
    console.error(error)
  }) 
  
example
.then((result) => {
     
 }).catch((err) => {
     
 }); 
example; fectapi //no id for post use only method :delete for deletion
//filter is also possible 
//jquery https://htmlcheatsheet.com/jquery/
fetch('https://jsonplaceholder.typicode.com/posts?userId=1')
fetch('https://jsonplaceholder.typicode.com/posts/1', {
    method: 'PUT',
    body: JSON.stringify({
      id: 1,
      title: 'foo',
      body: 'bar',
      userId: 1
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then(response => response.json())
  .then(json => console.log(json))

  $(document).ready(function(){
    $("button").click(function(){
      $.post("demo_test_post.asp",
      {
        name: "Donald Duck",
        city: "Duckburg"
      },
      function(data,status){
        alert("Data: " + data + "\nStatus: " + status);
      });
    });
  });



  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script>
  $(document).ready(function(){
    $("button").click(function(){
      $("#div1").load("demo_test.txt", function(responseTxt, statusTxt, xhr){
        if(statusTxt == "success")
          alert("External content loaded successfully!");
        if(statusTxt == "error")
          alert("Error: " + xhr.status + ": " + xhr.statusText);
      });
    });
  });
  </script>
  </head>
  <body>
  
  <div id="div1"><h2>Let jQuery AJAX Change This Text</h2></div>
  
  <button>Get External Content</button>
   example
   fetch('http://nikola-breznjak.com/_testings/ajax/test1.php?ime=Nikola')
  .then(function(response) {
    return response.text();
  })
  .then(function(text) {
    $('#result').html(text);
  }); 

  example
  var link = 'http://nikola-breznjak.com/_testings/ajax/test2.php';
fetch(link)
    .then(function(response){
        return response.json()
    })
    .then(function(result){
        var oglasiHTML = '';
        $.each(result, function(index, oglas){
            var klasaCijene = '';
            if (oglas.cijena < 100){
                klasaCijene = 'is-success';
            }
            else if (oglas.cijena >= 100 && oglas.cijena < 300){
                klasaCijene = 'is-info';
            }
            else if (oglas.cijena >= 300){
                klasaCijene = 'is-danger';
            }

            oglasiHTML += `
                <div class="columns">
                    <div class="column is-one-quarter">
                        <span class="tag ${klasaCijene}">${oglas.cijena}</span>
                    </div>
                    <div class="column">${oglas.tekst}</div>
                </div>
            `;
        });

        $('#oglasi').html(oglasiHTML);
    });

    var myData = {
    hello: 1
};


fetch("/api/v1/endpoint/5/", {
    method: "put",
    credentials: "same-origin",
    headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    body: JSON.stringify(myData)
}).then(function(response) {
    return response.json();
}).then(function(data) {
    console.log("Data is ok", data);
}).catch(function(ex) {
    console.log("parsing failed", ex);
});