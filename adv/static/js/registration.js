let users = { "teslestien@gmail.com": "123456", "kt@gmail.com": "password" }
var email;
var password;
document.getElementById("login").style.display = "none";
document.getElementById("edit").style.display = "none";

function register() {
   var email = document.getElementById("remail").value;
   var password = document.getElementById("rpassword").value;
   users[email] = password;
   document.getElementById("registration").style.display = "none";
   document.getElementById("login").style.display = "block";
}
function login() {
   email = document.getElementById("lemail").value;
   password = document.getElementById("lpassword").value;
   if (users[email] == password) {
      document.getElementById("edit").style.display = "block";
      document.getElementById("eemail").innerHTML = email;
      document.getElementById("epassword").innerHTML = password;
   }
   else {
      document.getElementById("edit").style.display = "none";
      alert("Invalid email or password");
   }
}

function edit() {
   delete users[email]
   users[document.getElementById("eemail").innerHTML] = document.getElementById("epassword").innerHTML;
   document.getElementById("edit").style.display = "none";
   document.getElementById("login").style.display = "block";
}