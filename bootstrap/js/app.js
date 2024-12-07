// Custom JavaScript
document.addEventListener("DOMContentLoaded", () => {
    console.log("Page loaded!");

    // Add event listener to the contact form submit button
    document.getElementById("contact-submit").addEventListener("click", (e) => {
        e.preventDefault(); // Prevent form submission for demo
        alert("Form submitted! We'll get back to you shortly.");
    });
});

