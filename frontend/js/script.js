let timer;
document.getElementById("inputText").addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(sendText, 600); // debounce
});


async function sendText() {
    let text = document.getElementById("inputText").value;
    if (text.trim() === "") {
        document.getElementById("correctedText").innerText = "";
        return;
    }

    let response = await fetch("/fix_grammar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });
    let data = await response.json();
    document.getElementById("correctedText").innerText = data.corrected;
}