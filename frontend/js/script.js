let timer;
document.getElementById("inputText").addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(sendText, 600); // debounce
});


async function sendText() {
    const text = document.getElementById("inputText").value;
    if (!text.trim()) {
        document.getElementById("diffOutput").innerHTML = "";
        return;
    }

    const resp = await fetch("/process_text", {
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
