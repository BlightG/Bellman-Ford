function removeEdge() {
    let edgeContainer = document.getElementById('edge-container');
    let inputElements = edgeContainer.querySelectorAll('input');  // Get all input elements
    if (inputElements.length > 0) {
        let lastInput = inputElements[inputElements.length - 1];  // Get the last input element
        lastInput.remove();  // Remove the last input
    }
}