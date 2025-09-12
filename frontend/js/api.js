// api.js - handles communication with the backend.

export async function improveText(text) {
    const response = await fetch("/edit_text", {
        method: "POST",
        headers: {
            "accept": "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: text
        })
    });

    if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
    }
    return response.json();
}

export async function fixSpellingRequest(text) {
    const resp = await fetch("/fix_spelling", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    if (!resp.ok) {
        throw new Error(`Server error: ${resp.status}`);
    }
    return resp.json(); // { old_text, no_spelling_text }
}
