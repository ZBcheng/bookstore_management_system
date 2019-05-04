function login() {
    var elem = document.getElementById('modal1')
    var instances = M.Modal.init(elem)
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    console.log(username)
    console.log(password)
    if(username == "") {
        var elem = document.getElementById('modal1')
        var instances = M.Modal.init(elem)
    } else {
        document.getElementById("log_form").submit()
    }
}






