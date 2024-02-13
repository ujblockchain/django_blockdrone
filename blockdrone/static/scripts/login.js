import { initializeApp } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-app.js";
import {
  getDatabase,
  ref,
  get,
  child
} from "https://www.gstatic.com/firebasejs/10.6.0/firebase-database.js";
import {
  getAuth,
  signInWithEmailAndPassword
} from "https://www.gstatic.com/firebasejs/10.6.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyBozEVVdZQzb1YHdv6LM-5y7o1YtM4IYVE",
  authDomain: "block-drones.firebaseapp.com",
  projectId: "block-drones",
  storageBucket: "block-drones.appspot.com",
  messagingSenderId: "525472458043",
  appId: "1:525472458043:web:5f3b85532994c65c8e831e"
};

const app = initializeApp(firebaseConfig);
const database = getDatabase();
const auth = getAuth(app);
const databaseref = ref(database);

const email = document.getElementById('email');
const password = document.getElementById('password');
const FORM = document.getElementById('form');

//Login user function
const login = (event) => {{
  event.preventDefault();

  signInWithEmailAndPassword(auth, email.value, password.value)
  .then((credentials) => {
    get(child(databaseref, 'users/' + credentials.user.uid))
      .then((snapshot) => {
        if (snapshot.exists()) {
          sessionStorage.setItem('user-info', JSON.stringify({
            firstName: snapshot.val().firstName,
            surname: snapshot.val().surname,
            email: snapshot.val().email,
            type: snapshot.val().type,
            uid: snapshot.val().uid,
            imageUrl: snapshot.val().imageUrl,
            createdAt: snapshot.val().createdAt
          }));

          sessionStorage.setItem('user-creds', JSON.stringify(credentials.user));
          sessionStorage.setItem('signedIn','true');

          window.location.href = '../profile/dashboard.html';
        } else {
          console.log('No data available');
        }
      })
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;

    alert(`${errorCode}: ${errorMessage}`);
    console.log(errorCode);
    console.log(errorMessage);
  });

  FORM.reset();
}}

FORM.addEventListener('submit', login);