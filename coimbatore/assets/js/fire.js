
    // Import the functions you need from the SDKs you need
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.3.0/firebase-app.js";
    import { getDatabase, ref, child, get, set, onValue } from "https://www.gstatic.com/firebasejs/10.3.0/firebase-database.js";

    const firebaseConfig = {
        apiKey: "AIzaSyBI_KYCnyVtRKkzBD42sLnFMMMoW6baIYI",
        authDomain: "green-house-monitoring-d4689.firebaseapp.com",
        databaseURL: "https://green-house-monitoring-d4689-default-rtdb.firebaseio.com",
        projectId: "green-house-monitoring-d4689",
        storageBucket: "green-house-monitoring-d4689.appspot.com",
        messagingSenderId: "971383452008",
        appId: "1:971383452008:web:cf0174fa19e53790d066dd",
        measurementId: "G-SFGW7H4BMJ"
    };

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    const database = getDatabase(app);

    const dbRef = ref(getDatabase(app));


    var starCountRef = ref(database, '/Greenhouse gas/CO2');
    onValue(starCountRef, (snapshot) => {
        var data = snapshot.val();
        document.getElementById("co2").innerHTML = snapshot.val();
    });

    var starCountRef = ref(database, '/Greenhouse gas/NH3');
    onValue(starCountRef, (snapshot) => {
        var data = snapshot.val();
        document.getElementById("nh3").innerHTML = snapshot.val();
    });

    var starCountRef = ref(database, '/Greenhouse gas/Benzene PPM');
    onValue(starCountRef, (snapshot) => {
        var data = snapshot.val();
        document.getElementById("bz").innerHTML = snapshot.val();
    });

    var starCountRef = ref(database, '/Greenhouse gas/Carbon Monoxide PPM');
    onValue(starCountRef, (snapshot) => {
        var data = snapshot.val();
        document.getElementById("CO").innerHTML = snapshot.val();
    });
