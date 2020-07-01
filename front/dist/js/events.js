window.onload = function () {

    document.getElementById("btnlogin").addEventListener("click", loginfunc, true);

    document.getElementById("btnregist").addEventListener("click", registfunc, true);

}

function loginfunc(event) {
    event.preventDefault();

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
                    sessionStorage.setItem("GEV_OVA_USER_TOKEN", token);
                    console.log(token);
                    let aser = atob(token.split('.')[1])
                    console.log(aser)

                    let re = JSON.parse(aser);
                    sessionStorage.setItem("GEV_OVA_USER_DATA", aser);
                    console.log(re.tipo)

                    switch (re.tipo) {
                        case '1':
                            location.href = "ovaresources/gev/index.html";
                            break;
                        case '2':
                            location.href = "docente/main.html";
                            break;
                        case '3':
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


function registfunc(event) {
    event.preventDefault();
    const url = serverurl + 'registro';
    let nom = document.getElementById('registnom').value;
    let apell = document.getElementById('registapell').value;
    let email = document.getElementById('registEmail').value;
    let passw = document.getElementById('registPass').value;
    let verypass = document.getElementById('verifyPass').value;
    let tip = document.getElementById('tipousr').value;
    

    if(verypass==passw){
        let data = 
        {
            nombre : nom,
            apellido : apell,
            correo : email,
            contraseña : passw,
            tipo:tip
        }


        let init = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        };

        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            console.log(data)
            let msjdiv = document.getElementById("msjrecu");
            msjdiv.insertAdjacentHTML('afterbegin', '<div class="alert alert-success alert-dismissible">' +
                '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' +
                '<h5><i class="icon fas fa-check"></i> Alert!</h5>' +
                'se ha registrado correctamente </div>');

        })
        .catch(function (err) {
            let msjdiv = document.getElementById("msjrecu");
            msjdiv.insertAdjacentHTML('afterbegin', '<div class="alert alert-warning alert-dismissible">' +
                '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' +
                '<h5><i class="icon fas fa-exclamation-triangle"></i> Alert!</h5>' +
                'error de conexion , no se puede conectar con el servidor</div>');
        });
    }      

}