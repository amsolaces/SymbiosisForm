function validateForm() {
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm").value;
  const gender = document.querySelector('input[name="gender"]:checked');
  const course = document.getElementById("course").value;

  if (!name) {
    alert("Name cannot be empty");
    return false;
  }

  if (!email) {
    alert("Email cannot be empty");
    return false;
  }

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    alert("Please enter a valid email address");
    return false;
  }

  if (!password || password.length < 6) {
    alert("Password must be at least 6 characters");
    return false;
  }

  if (password !== confirmPassword) {
    alert("Passwords do not match");
    return false;
  }

  if (!gender) {
    alert("Please select your gender");
    return false;
  }

  if (!course) {
    alert("Please select a course");
    return false;
  }

  alert("Registration Successful");
  return true;
}
