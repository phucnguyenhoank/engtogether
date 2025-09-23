// utils.js - General-purpose helpers (not tied to UI or API).
export function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

export function pickStyleEndpoint(tags) {
    let style = "neutral"; // default

    for (const tag of tags) {
        if (tag.name.toLowerCase() === "formal") {
            style = "formal";
            break;
        }
        if (tag.name.toLowerCase() === "informal") {
            style = "informal";
            break;
        }
    }

    switch (style) {
        case "formal":
            return "make_formal";
        case "informal":
            return "make_informal";
        default:
            return "make_neutral";
    }
}
