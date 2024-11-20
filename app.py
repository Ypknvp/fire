// Register new user
function register() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  auth.createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // User is registered
      document.getElementById('login-register-form').style.display = "none";
      document.getElementById('name-input-form').style.display = "block";
      console.log("User registered:", userCredential.user);
    })
    .catch((error) => {
      document.getElementById('auth-error').innerText = error.message;
    });
}

// Login existing user
function login() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  auth.signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // User is logged in
      document.getElementById('login-register-form').style.display = "none";
      document.getElementById('name-input-form').style.display = "block";
      console.log("User logged in:", userCredential.user);
    })
    .catch((error) => {
      document.getElementById('auth-error').innerText = error.message;
    });
}

// Save the user's name to Firestore
function saveName() {
  const userName = document.getElementById('name').value;
  const user = auth.currentUser;

  if (user) {
    // Save the name to Firestore under user's document
    db.collection('users').doc(user.uid).set({
      name: userName
    })
    .then(() => {
      alert('Name saved successfully!');
      console.log("Name saved to Firestore:", userName);
    })
    .catch((error) => {
      alert('Error saving name: ' + error.message);
    });
  } else {
    alert('User not authenticated');
  }
}
