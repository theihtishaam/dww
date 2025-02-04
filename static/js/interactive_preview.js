// static/js/interactive_preview.js
// Stub for interactive preview selection tool.
// In a production system, integrate a library (e.g., interact.js) for element selection.
document.addEventListener("DOMContentLoaded", function() {
    const previewFrame = document.getElementById("previewFrame");
    if (previewFrame) {
        previewFrame.contentWindow.document.addEventListener("click", function(e) {
            e.preventDefault();
            let selectedId = e.target.id;
            if (selectedId) {
                console.log("Selected element ID:", selectedId);
                // In a full implementation, send the selection info to the backend via fetch or socket.emit.
            }
        });
    }
});
