// script.js
// Function to handle file upload and display result
function handleFileUpload(event) {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    // Show loading spinner
    document.getElementById('result-container').style.display = 'none';
    document.getElementById('result-value').textContent = '';
    document.body.style.cursor = 'wait';

    // Send AJAX request to server
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // Hide loading spinner and display result
            document.getElementById('result-container').style.display = 'block';
            document.getElementById('result-value').textContent = xhr.responseText;
            document.body.style.cursor = 'default';
        }
    };
    xhr.send(formData);
}

// Add event listener to file input
const fileInput = document.querySelector('input[type="file"]');
fileInput.addEventListener('change', handleFileUpload);

// Add event listener to button
const btn = document.querySelector('.btn');
btn.addEventListener('click', () => {
    fileInput.click();
});