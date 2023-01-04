var password =document.getElementById("password");
var confirm=document.getElementById("confirm_password");
function validatepassword(){
  if(password.value !=confirm_password.value)
  {
    confirm_password.setCustomValidity("Password Dont Match");
  }
    
  else{
    confirm_password.setCustomValidity('');
  }
}
password.onchange=validatepassword;
confirm_password.onkeyup=validatepassword;

