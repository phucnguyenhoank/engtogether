// ui.js - handles DOM rendering and event binding.
import { fixGrammar, improveText, fetchExercises } from "./api.js";
import { debounce, pickStyleEndpoint } from "./utils.js";

let exercises = []; // will be loaded dynamically


export async function showHomePage() {
    const main = document.getElementById("main-content");
    main.innerHTML = "<h2>Your exercises today</h2>";

    try {
        exercises = await fetchExercises(); // fetch from backend

        exercises.forEach(ex => {
            // Create a container card
            let card = document.createElement("div");
            card.className = "exercise-card";

            // Title (clickable)
            let title = document.createElement("h3");
            title.innerText = ex.title;
            title.className = "exercise-title";
            title.addEventListener("click", () => showExercisePage(ex));

            // Description
            let desc = document.createElement("p");
            desc.innerText = ex.description;
            desc.className = "exercise-desc";

            // Tags
            let tags = document.createElement("div");
            tags.className = "exercise-tags";
            ex.tags.forEach(tag => {
                let span = document.createElement("span");
                span.className = "tag";
                span.innerText = tag.name + " - " + tag.score;
                tags.appendChild(span);
            });

            // Append to card
            card.appendChild(title);
            card.appendChild(desc);
            card.appendChild(tags);

            // Append card to page
            main.appendChild(card);
        });
    } catch (err) {
        main.innerHTML += `<p class="error">❌ Failed to load exercises: ${err.message}</p>`;
    }
}


export function showExercisePage(exercise) {
    const main = document.getElementById("main-content");
    main.innerHTML = `
        <h4>${exercise.title}</h4>
        <p>${exercise.description}</p>
        <textarea id="exerciseText" rows="6" cols="60" placeholder="Start writing..."></textarea>
        <p id="diffOutput"></p>
        <button id="improveBtn">Improve</button>
    `;

    // "Improve" → simplify text
    document.getElementById("improveBtn").addEventListener("click", () => handleImprove(exercise));

    // Grammar fixing (live, replaces spelling)
    const debouncedFixGrammar = debounce(handleFixGrammar, 600);
    document.getElementById("exerciseText").addEventListener("input", debouncedFixGrammar);
}


async function handleImprove(exercise) {
    const text = document.getElementById("exerciseText").value;
    const output = document.getElementById("diffOutput");

    if (!text.trim()) {
        output.innerText = "⚠️ Please write something first!";
        return;
    }

    output.innerText = "⏳ Improving...";
    try {
        const endpoint = pickStyleEndpoint(exercise.tags);
        const data = await improveText(text, endpoint);
        const diffs = Diff.diffWords(data.old_text, data.improved_text);

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


async function handleFixGrammar() {
    const text = document.getElementById("exerciseText").value.trim();
    const output = document.getElementById("diffOutput");

    if (!text) {
        output.innerHTML = "";
        return;
    }

    try {
        const data = await fixGrammar(text);
        const diffs = Diff.diffWords(data.old_text, data.improved_text);

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
