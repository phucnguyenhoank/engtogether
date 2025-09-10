// ---------------
// EDIT TEXT
// ---------------
async function editText() {
    const text = document.getElementById("inputText").value;
    if (!text.trim()) {
        document.getElementById("diffOutput").innerHTML = "";
        return;
    }

    const resp = await fetch("/edit_text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await resp.json();
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
}


// debounce helper
function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// ---------------
// SPELLING CHECK
// ---------------
async function fixSpelling() {
    const text = document.getElementById("inputText").value.trim();
    if (!text) {
        document.getElementById("diffOutput").innerHTML = "";
        return;
    }

    const resp = await fetch("/fix_spelling", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await resp.json();
    const oldText = data.old_text;
    const newText = data.no_spelling_text; // or corrected_text

    const diffs = Diff.diffWords(oldText, newText);
    let html = "";
    diffs.forEach(part => {
        if (part.added) {
            html += `<span class="added">${part.value}</span>`;
        } else if (part.removed) {
            html += `<span class="removed">${part.value}</span>`;
        } else {
            html += part.value;
        }
    });

    document.getElementById("diffOutput").innerHTML = html;
}

// debounce for 500ms after user stops typing
const debouncedFixSpelling = debounce(fixSpelling, 500);

// attach to textarea
document.getElementById("inputText").addEventListener("input", debouncedFixSpelling);
