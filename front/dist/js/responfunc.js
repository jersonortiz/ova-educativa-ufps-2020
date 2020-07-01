function responsesend(datares) {
    console.log("enviar")
    userdat = sessionStorage.getItem("GEV_OVA_USER_DATA");
    token = sessionStorage.getItem("GEV_OVA_USER_TOKEN");

    let url = serverurl + 'responder';
    console.log(url)

    let data = datares;
    console.log(JSON.stringify(data));
    console.log(token);

    let init = {
        method: 'POST',
        headers: {
            mode: 'cors',
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': token
        },
        body: JSON.stringify(data),
        cache: 'default'
    };

    fetch(url, init)
            .then((resp) => resp.json())
            .then(function (data) {
                if (data) {

                    console.log(data);

                } else {
                    console.log(data);
                }
            })
            .catch(function (err) {
                console.log(err);

            });

}