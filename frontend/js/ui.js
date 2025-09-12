// ui.js - handles DOM rendering and event binding.
import { improveText } from "./api.js";
import { fixSpellingRequest } from "./api.js";
import { debounce } from "./utils.js";

export const exercises = [
    "Describe your family",
    "What makes you happy most?",
    "Write about your favorite hobby",
    "Describe your favorite food"
];

export function showHomePage() {
    const main = document.getElementById("main-content");
    main.innerHTML = "<h2>Top exercises today</h2>";

    exercises.forEach(exercise => {
        let exercise_title = document.createElement("h4");
        exercise_title.innerText = exercise;
        exercise_title.addEventListener("click", () => showExercisePage(exercise));
        main.appendChild(exercise_title);
    });
}

export function showExercisePage(exercise) {
    const main = document.getElementById("main-content");
    main.innerHTML = `
        <h4>${exercise}</h4>
        <textarea id="exerciseText" rows="6" cols="60" placeholder="Start writing..."></textarea>
        <p id="diffOutput"></p>
        <button id="improveBtn">Improve</button>
    `;

    // coedit text
    document.getElementById("improveBtn").addEventListener("click", handleImprove);

    // spelling
    const debouncedFixSpelling = debounce(handleFixSpelling, 500);
    document.getElementById("exerciseText").addEventListener("input", debouncedFixSpelling);
}

async function handleImprove() {
    const text = document.getElementById("exerciseText").value;
    const output = document.getElementById("diffOutput");

    if (!text.trim()) {
        output.innerText = "⚠️ Please write something first!";
        return;
    }

    output.innerText = "⏳ Improving...";
    try {
        const data = await improveText(text);
        const oldText = data.old_text;
        const newText = data.improved_text;

        const diffs = Diff.diffWords(oldText, newText);
        let html = "";
        diffs.forEach(part => {
            if (part.added) {
                html += `<span class="added">${part.value}</span>`;
            } else if (part.removed) {
                html += `<span class="removed">${part.value}</span>`;
            } else {
                html += part.value; // unchanged
            }
        });

        document.getElementById("diffOutput").innerHTML = html;
    } catch (err) {
        output.innerText = "❌ Error: " + err.message;
    }
}

async function handleFixSpelling() {
    const text = document.getElementById("exerciseText").value.trim();
    const output = document.getElementById("diffOutput");

    if (!text) {
        output.innerHTML = "";
        return;
    }

    try {
        const data = await fixSpellingRequest(text);
        const diffs = Diff.diffWords(data.old_text, data.no_spelling_text);

        let html = "";
        diffs.forEach(part => {
            if (part.added) html += `<span class="added">${part.value}</span>`;
            else if (part.removed) html += `<span class="removed">${part.value}</span>`;
            else html += part.value;
        });

        output.innerHTML = html;
    } catch (err) {
        output.innerText = "❌ Error: " + err.message;
    }
}
