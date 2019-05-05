function login() {
    var elem = document.getElementById('modal1')
    var instances = M.Modal.init(elem)
    var store_name = document.getElementById("store_name").value
    var password = document.getElementById("password").value
    console.log(store_name)
    console.log(password)
    if(store_name == "") {
        // var elem = document.getElementById('modal1')
        // var instances = M.Modal.init(elem)
    } else {
        document.getElementById("log_form").submit()
    }
}






