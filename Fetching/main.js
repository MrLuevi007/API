fetch('http://7978-223-190-3-78.ngrok.io/').then(
    res =>{
        res.json().then(
            data=>{
                console.log(data);
                if(data.length >0){
                    var temp = '';

                    data.forEach((u) => {
                        temp += "<tr>";
                        temp += "<td>"+u.fname+"</td>";
                        temp += "<td>"+u.lname+"</td>";
                        temp += "<td>"+u.timestamp+"</td></tr>";
                    })
                    document.getElementById("data").innerHTML = temp;
                }
            }
        )
    }
)