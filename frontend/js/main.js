// main.js - entry point that wires everything together.
import { showHomePage } from "./ui.js";

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("homeBtn").addEventListener("click", showHomePage);
    showHomePage();
});
