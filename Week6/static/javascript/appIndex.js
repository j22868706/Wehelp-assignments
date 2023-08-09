function submitForm(event) {
  event.preventDefault(); 
  
  let nameInput = document.getElementById("user_name");
  let usernameInput = document.getElementById("user_username");
  let passwordInput = document.getElementById("user_password");
  
  if (nameInput.value === "" || usernameInput.value === "" || passwordInput.value === "") {
    alert("Looks like you missed something. Please fill in all fields!");
  } else {
    document.getElementById("signupForm").submit();
  }
}
