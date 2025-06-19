import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyA6t_XwQRXHMX04-Hc6xnOEryDnBQLwBcQ",
  authDomain: "vimarsha-9fa29.firebaseapp.com",
  projectId: "vimarsha-9fa29",
  storageBucket: "vimarsha-9fa29.appspot.com",
  messagingSenderId: "946831654968",
  appId: "1:946831654968:web:c5ccdca18df262e22566cd",
  measurementId: "G-H1M121KW31",
};

const app = initializeApp(firebaseConfig);

export const storage = getStorage(app);
export const db = getFirestore(app);
