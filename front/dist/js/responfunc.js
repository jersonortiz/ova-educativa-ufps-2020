
function responsesend() {
    event.preventDefault();
    userdat= sessionStorage.getItem("GEV_OVA_USER_DATA");
    token= sessionStorage.getItem("GEV_OVA_USER_TOKEN");

    let url = serverurl + 'login';
    let usr = document.getElementById("txtUser").value;
    let pass = document.getElementById("txtPass").value;
    let auth = {};
    let data = {user: usr, password: pass};
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

                    switch (re.tipo) {
                        case 1:
                            location.href = "ovaresources/gev/index.html";
                            break;
                        case 2:
                            location.href = "docente/dashboard.html";
                            break;
                        case 3:
                            location.href = "admin/dashboard.html";
                            break;
                    }
                    
                } else {

                    let msjdiv = document.getElementById("msjerr");
                    msjdiv.insertAdjacentHTML('afterbegin', '<div class="alert alert-warning alert-dismissible">' +
                            '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' +
                            '<h5><i class="icon fas fa-exclamation-triangle"></i> Alert!</h5>' +
                            'contraseña incorreta</div>');
                }
            })
            .catch(function (err) {
                console.log(err);
                let msjdiv = document.getElementById("msjerr");
                msjdiv.insertAdjacentHTML('afterbegin', '<div class="alert alert-warning alert-dismissible">' +
                        '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' +
                        '<h5><i class="icon fas fa-exclamation-triangle"></i> Alert!</h5>' +
                        'error de conexion , no se puede conectar con el servidor</div>');
            });

}