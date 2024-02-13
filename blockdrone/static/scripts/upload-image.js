const firebaseConfig = {
  apiKey: "AIzaSyBozEVVdZQzb1YHdv6LM-5y7o1YtM4IYVE",
  authDomain: "block-drones.firebaseapp.com",
  projectId: "block-drones",
  storageBucket: "block-drones.appspot.com",
  messagingSenderId: "525472458043",
  appId: "1:525472458043:web:5f3b85532994c65c8e831e"
};

firebase.initializeApp(firebaseConfig);

const INPUT = document.getElementById('avatar');
const UPLOAD = document.getElementById('upload');

console.log(firebase);

function uploadImage() {
  const ref = firebase.storage().ref();
  const file = INPUT.files[0];
  const name = +new Date() + "-" + file.name;
  const metadata = {
      contentType: file.type
  };
  const task = ref.child(name).put(file, metadata);task
  .then(snapshot => snapshot.ref.getDownloadURL())
  .then(url => {

  console.log(url);

  alert('image uploaded successfully');
  document.querySelector("#image").src = url;
})
.catch(console.error);
}

const errorMsgElement = document.querySelector('span#errorMsg');