/**
 * Wait for DOM to finish loading before running script
 * Code from Code Institute walkthrough project
 */
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
    
});