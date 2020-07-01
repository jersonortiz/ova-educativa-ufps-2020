let url = serverurl;
let userdat= JSON.parse(sessionStorage.getItem("GEV_OVA_USER_DATA"));
let token= sessionStorage.getItem("GEV_OVA_USER_TOKEN");

console.log(userdat);

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
            user:userdat,
            docentes:{docs:{},},
            gruposs:{grup:{},},
            seldocente:0,
            seldoc:true,
            selgru:false,
  
        },
        methods:
        {
            cargardocentes: cargardocentes,
            cargargrupos: cargargrupos,
            asignargrupo:asignargrupo,
            showgrupos:showgrupos,
            showdocentes:showdocentes,
  
        },
        created: cargardocentes,
        
    });


    function showdocentes(){
        vm.seldoc=true;
        vm.selgru=false;
    }

    function showgrupos(){
        vm.seldoc=false;
        vm.selgru=true;
    }
   
    function cargardocentes(){

        let data={nada:'#'}
        let url = serverurl + 'cargardocentes';
        let init =makeinit(data,token)

        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            if (data) {
                console.log(data);
                vm.docentes=data;
            }
        })
        .catch(function (err) {
            console.log(err);
        });
    }

    function cargargrupos(event){
        let docen = event.target.value;
        let data={docente:docen};
        vm.seldocente=docen
        let url = serverurl + 'gruposdocente';
        let init =makeinit(data,token);
        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            if (data) {
                console.log(data)
                vm.gruposs=data;
                showgrupos();
            }
        })
        .catch(function (err) {
            console.log(err);
        });
    }

    function asignargrupo(event){
        let grup =event.target.value;
        let doc = vm.seldocente
        data={grupo:grup , docente:doc , user:userdat.id};
        let url = serverurl + 'asignargrupo';
        let init =makeinit(data,token);
        fetch(url, init)
        .then((resp) => resp.json())
        .then(function (data) {
            if (data) {
                console.log(data)
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

}