window.onload = function(){
    let login_email = document.getElementById("id_login");
    let login_password = document.getElementById("id_password");

    if (login_email){
        login_email.classList.add("form-control");
    }

    if (login_password){
        login_password.classList.add("form-control");
    }
}