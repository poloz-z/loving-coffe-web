<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyACFCAVK8ZX4q6G3e3b0miG5URmcNXj9X0",
    authDomain: "loving-coffe.firebaseapp.com",
    projectId: "loving-coffe",
    storageBucket: "loving-coffe.appspot.com",
    messagingSenderId: "831003095514",
    appId: "1:831003095514:web:cf30d7e8729c1a10a610e3",
    measurementId: "G-0157T8Y5SC"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if false;
    }
  }
}