function buyBooks(btn) {
    var name = btn.parentNode.parentNode.firstChild.nextSibling.textContent
    var psel = document.getElementById("book_name");
    psel.value = name; //设置
    alert(psel.value)
    document.getElementById("log_form").submit()
}
