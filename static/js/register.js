function register() {
    var elem = document.getElementById('modal1')
    var instances = M.Modal.init(elem)
    var username = document.getElementById("username").value
    var name = document.getElementById('name').value
    var password = document.getElementById("password").value
    var email = document.getElementById('email').values
    var birthday = document.getElementById('birthday').value
    var mobile = document.getElementById('mobile').value
    console.log(username)
    console.log(password)
    console.log(email)
    console.log(mobile)
    if(username == "") {
        var elem = document.getElementById('modal1')
        var instances = M.Modal.init(elem)
    } else {
        document.getElementById("log_form").submit()
    }
}


