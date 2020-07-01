let url = serverurl;
let userdat= JSON.parse(sessionStorage.getItem("GEV_OVA_USER_DATA"));
let token= sessionStorage.getItem("GEV_OVA_USER_TOKEN");



if ((token == null) && (userdat == null)) {
    console.log('no hay sesion');
    location.href = "../login.html";

} else {
    console.log(token);
    console.log(url);
    console.log(JSON.stringify(userdat));

    window.onload = function () {

        document.getElementById("cerrars").addEventListener("click", function () {
            sessionStorage.removeItem("USER_TOKEN");
            location.href = "../login.html";
        });

    };

    const vm = new Vue({
        el: 'main',
        data:
        {
            user: userdat,
            grupos: {},
            list:true,
            regist:false,
            estudents:false,
            muestrapregestud:false,
            msjregistro:'',
            estudiantes:{},
            selectstudent:0,
            respuestasestudiante:{},
        },
        methods:
        {
            seleccionar: seleccion,
            cargargrupos: cargargrupos,
            creargrupo: creargrupo,
            showregistro:showregist,
            regresalistar:regresalistar,
            mostrarestudiante:mostrarestudiante,
            preguntasest:preguntasest,
            shostudents:shostudents,
        },
        created: cargargrupos,
    });


    function regresalistar(event) {
        vm.list = true;
        vm.regist = false;
        vm.estudents = false;
        vm.muestrapregestud=false;
    }

    function showregist(event){
        vm.regist = true;
        vm.list = false;
        vm.estudents = false;
        vm.muestrapregestud=false;

    }

    function shostudents(){
        vm.estudents = true;
        vm.regist = false;
        vm.list = false;
        vm.muestrapregestud=false;

    }

    function preguntasest(event){
        let tema = event.target.value;
        let estid = vm.selectstudent;

        let data={idest:estid, tema:tema}
        let url = serverurl + 'respuestasestudiante';
        let init =makeinit(data,token)
        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            if (data) {
                console.log(data);
                vm.respuestasestudiante=data;
            }
        })
        .catch(function (err) {
            console.log(err);
        });
    }

    function mostrarestudiante(event){
        let idest=event.target.value;
        vm.selectstudent = idest;
        vm.estudents = false;
        vm.regist = false;
        vm.list = false;
        vm.muestrapregestud=true;

    }

    function seleccion(event) {
        let grupoid=event.target.value;
        let data={idg:grupoid}
        let url = serverurl + 'estudiantesgrupo';
        let init =makeinit(data,token)
        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            if (data) {
                console.log(data);
                vm.estudiantes=data;
                shostudents()

            }
        })
        .catch(function (err) {
            console.log(err);
        });
    }

    function makeinit(data, authToken) {
        let heads = new Headers();
        heads.append("Accept", "application/json");
        heads.append("Content-Type", "application/json");
        heads.append("Access-Control-Allow-Origin", "*");
        heads.append("Authorization", authToken);
        let init = {
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(data),
            headers: heads,
            cache: 'default'
        };
        return init;
    }

    function cargargrupos(){
        console.log("cargargrupos")

        let data={nada:'#'}
        let url = serverurl + 'grupos';
        let init =makeinit(data,token)

        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            if (data) {
                vm.grupos=data
            }
        })
        .catch(function (err) {
            console.log(err);
        });
    }

    function creargrupo(){

        let url = serverurl + 'creargrupo';
        let nom = document.getElementById('txtgrupo').value;
        let data={nombre:nom}
        let init =makeinit(data,token)
    
        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            if (data) {
                console.log(data)
                switch (data.status) {
                    case 'existe':
                        vm.msjregistro="el grupo ya existe"
                        break;
                    case 'registered':
                        vm.msjregistro="el grupo fue registrado"
                        break;
                    case 'fail':
                        vm.msjregistro="hubo un problema al registrar"
                        break;
                }        
                
            } else {
                console.log('eh');
            }
        })
        .catch(function (err) {
            console.log(err);
        });


    }



}