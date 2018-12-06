  import firebase from 'firebase'
  
  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyDdq6XcKi_SUi7jteINyWfo2tAf4j_00-w",
    authDomain: "computacionfisica-49742.firebaseapp.com",
    databaseURL: "https://computacionfisica-49742.firebaseio.com",
    projectId: "computacionfisica-49742",
    storageBucket: "computacionfisica-49742.appspot.com",
    messagingSenderId: "578433874706"
  };

  firebase.initializeApp(config);

  export default firebase;