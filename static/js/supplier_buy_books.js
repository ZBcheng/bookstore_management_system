function buyBooks(btn) {
    var name = btn.parentNode.parentNode.firstChild.nextSibling.textContent
    var psel = document.getElementById("book_name");
    var store_name = document.getElementById("store_name").value
    psel.value = name; //设置
    alert(store_name)
    document.getElementById("log_form").submit()
}
