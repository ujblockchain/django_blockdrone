import { initializeApp } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-app.js";
import {
  getDatabase,
  set,
  ref,
} from "https://www.gstatic.com/firebasejs/10.6.0/firebase-database.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
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

const firstName = document.getElementById('firstName');
const surname = document.getElementById('surname');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
const type = document.getElementById('type');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirmPassword');
const SIGNUP_FORM = document.getElementById('form');

const register = async (event) => {{
  event.preventDefault();

  if (!validatePassword(password.value, confirmPassword.value)) {
    alert('Passwords do not match');
    return;
  }

  try {
    const credentials = await createUserWithEmailAndPassword(
      auth,
      email.value,
      password.value
    );

    await set(ref(database, 'users/' + credentials.user.uid), {
      firstName: firstName.value,
      surname: surname.value,
      email: email.value,
      phone: phone.value,
      type: type.value,
      imageUrl: "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png",
      createdAt: new Date().toString(),
    });

    window.location.href = '../../index.html';
  } catch (error) {
    const errorCode = error.code;
    const errorMessage = error.message;
    
    alert(`${errorCode}: ${errorMessage}`);
    console.error(errorCode, errorMessage);
  }
  
  SIGNUP_FORM.reset();
}}

SIGNUP_FORM.addEventListener('submit', register);

function validatePassword(password, confirmPassword) {
  return password === confirmPassword;
}