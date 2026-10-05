"use strict";
/**
 * Mogaha Chioma Vivian — portfolio interactivity.
 * Two small, deliberate behaviors. The page's one orchestrated motion
 * moment is the hero's CSS entrance; nothing here duplicates it, and
 * nothing here can leave content stuck invisible if a browser quirk
 * skips an event.
 *  1. Mobile nav toggle
 *  2. Copy-email-to-clipboard button with a confirmation state
 */
function initNavToggle() {
    const toggle = document.getElementById("navToggle");
    const navList = document.getElementById("navList");
    if (!toggle || !navList)
        return;
    toggle.addEventListener("click", () => {
        const isOpen = navList.classList.toggle("open");
        toggle.setAttribute("aria-expanded", String(isOpen));
    });
    navList.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navList.classList.remove("open");
            toggle.setAttribute("aria-expanded", "false");
        });
    });
}
function initCopyEmail() {
    const button = document.getElementById("copyEmailBtn");
    if (!button)
        return;
    const email = button.dataset.email;
    if (!email)
        return;
    const defaultLabel = button.textContent ?? "Copy email address";
    button.addEventListener("click", async () => {
        try {
            await navigator.clipboard.writeText(email);
            button.textContent = "Copied to clipboard";
            button.dataset.copied = "true";
        }
        catch {
            // Clipboard access can fail (older browsers, denied permission).
            // Falling back to a mailto link keeps the button useful either way.
            window.location.href = `mailto:${email}`;
            return;
        }
        window.setTimeout(() => {
            button.textContent = defaultLabel;
            delete button.dataset.copied;
        }, 2200);
    });
}
function init() {
    initNavToggle();
    initCopyEmail();
}
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
}
else {
    init();
}
