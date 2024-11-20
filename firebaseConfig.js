
// Firebase Configuration
const firebaseConfig = {
    apiKey: "AIzaSyALc3uM6yfk8k26XVZ0vdUn9DRjN6DeDbs", // Replace with your API key
    authDomain: "godyog-fd295.firebaseapp.com",
    projectId: "godyog-fd295",
    storageBucket: "godyog-fd295.appspot.com",
    messagingSenderId: "730397639050",
    appId: "1:730397639050:web:559b4cef7c4ec670370873",
    measurementId: "G-72832EDYWR"
  };
  
  // Initialize Firebase
  const app = firebase.initializeApp(firebaseConfig);
  const auth = firebase.auth();
  const db = firebase.firestore();
  