document.addEventListener("DOMContentLoaded", function () {
    // Remove the System Settings option
    document
        .querySelectorAll('[data-mode="auto"]')
        .forEach(function (element) {
            element.remove();
        });
});