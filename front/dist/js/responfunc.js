
function responsesend(datares) {
    event.preventDefault();
    userdat= sessionStorage.getItem("GEV_OVA_USER_DATA");
    token= sessionStorage.getItem("GEV_OVA_USER_TOKEN");

    let url = serverurl + 'responder';

    let data = datares;
    console.log(data);

    let init = {
        method: 'POST',
        headers: {
            mode: 'cors',
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(data),
        cache: 'default'
    };

    fetch(url, init)
            .then((resp) => resp.json())
            .then(function (data) {
                if (data) {
                    let token = data.token;
                    sessionStorage.setItem("USER_TOKEN", token);
                    console.log(token);

                    let re = JSON.parse(atob(token.split('.')[1]));
                    console.log(re)
                    console.log(re.correo)

               
                    
                } else {

                 
                }
            })
            .catch(function (err) {
                console.log(err);
        
            });

}