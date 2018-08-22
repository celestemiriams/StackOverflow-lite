function validateForm() {
    var user_name = document.forms["signup-form"]["username"].value;
    var Email = document.forms["signup-form"]["email"].value;
    var pwd = document.forms["signup-form"]["password"].value;

    if (user_name == "") {
        alert("Please enter a User name");
        user_name.focus();
        return false;
    }
    if (Email == "") {
        alert("Please enter your Email");
        Email.focus();
        return false;
    }
    if (pwd == "") {
        alert("Please enter a password");
        pwd.focus();
        return false;
    }

}