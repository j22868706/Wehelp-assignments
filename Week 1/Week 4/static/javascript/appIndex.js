function submitForm() {
    const checkbox = document.getElementById("check");

    if (checkbox.checked) {
        document.getElementById("signin-form").submit();
    } else {
        alert("Please check the checkbox first.");
        event.preventDefault();
    }
}
