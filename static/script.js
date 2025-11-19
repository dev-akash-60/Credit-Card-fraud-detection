const video = document.getElementById("intro-video");
const main = document.getElementById("main-content");
const bg = document.getElementById("bg-image");

function hideVideo() {

    // Fade video only (no blocking)
    video.classList.add("hidden");

    // Show content + bg
    bg.classList.add("show");
    main.classList.add("show");
}

// Fire normally when video ends
video.addEventListener("ended", hideVideo);

// Backup: hide after 8 seconds in case ended doesn't fire
setTimeout(() => {
    if (!video.classList.contains("hidden")) {
        hideVideo();
    }
}, 8000);
