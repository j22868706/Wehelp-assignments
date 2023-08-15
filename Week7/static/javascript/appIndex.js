function submitSignupForm(signupEvent) {
  signupEvent.preventDefault(); 
  
  let signupNameInput = document.getElementById("signupName");
  let signupUsernameInput = document.getElementById("signupUsername");
  let signupPasswordInput = document.getElementById("signupPassword");
  
  if (signupNameInput.value === "" || signupUsernameInput.value === "" || signupPasswordInput.value === "") {
    alert("Looks like you missed something. Please fill in all fields!");
  } else {
    document.getElementById("signupForm").submit();
  }
}

function submitSigninForm(signinEvent) {
  signinEvent.preventDefault(); 
  
  let signinUsernameInput = document.getElementById("signinUsername");
  let signinPasswordInput = document.getElementById("signinPassword");
  
  if (signinUsernameInput.value === "" || signinPasswordInput.value === "") {
    alert("Looks like you missed something. Please fill in all fields!");
  } else {
    document.getElementById("signinForm").submit();
  }
}