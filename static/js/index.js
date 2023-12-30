const splits=['split_0', 'split_1', 'split_2', 'split_3', 'split_4'];

$(function(){
    addSplits();
    splits.map(function get(i){getInfo(i)});
});

function addSplits() {
    splits.map(function appendBtn(split){
        var btn_a = document.createElement('a')
        btn_a.href="/annotate/"+split;
        var btn = document.createElement('button')
        btn.className = "btn btn-primary"
        btn.innerText = split
        btn.style.marginRight = "2%";
        btn_a.appendChild(btn)
        document.getElementById("choice").appendChild(btn_a)
    })
}

function addSummary(data){
   let tableBody = document.getElementById("tableBody");
   let row = document.createElement("tr");

   let c1 = document.createElement("td");
   let c2 = document.createElement("td");
   let c3 = document.createElement("td");

   c1.innerText = data['splitName']
   c2.innerText = data['numTotal']
   c3.innerText = data['numCompleted']

   row.appendChild(c1);
   row.appendChild(c2);
   row.appendChild(c3);

   tableBody.appendChild(row);  
}

function getInfo(split_name){
    $.ajax({
        type: "GET", 
        url: "/info/"+split_name, 
        cache: false,
        contentType: false,
        processData: false, 
        beforeSend: null,
        success: function(data){
            addSummary(data)
        },
        error: function (request, status, error) {
            console.log("Error : ", error)
        },
    });
}

