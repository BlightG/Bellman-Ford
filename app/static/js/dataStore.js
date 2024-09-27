document.addEventListener('DOMContentLoaded', function () {
    loadSavedForms(); // Load saved forms on page load
});

function saveForm() {
    let form = document.getElementById('dynamic-form');
    let formData = new FormData(form);
    let formValues = {};

    // Collect form values
    formData.forEach((value, key) => {
        if (!formValues[key]) {
            formValues[key] = [];
        }
        formValues[key].push(value);
    });

    // Save form to localStorage
    let savedForms = JSON.parse(localStorage.getItem('savedForms')) || [];
    savedForms.push(formValues);
    localStorage.setItem('savedForms', JSON.stringify(savedForms));

    // Reload saved forms
    loadSavedForms();
}

function loadSavedForms() {
    let savedForms = JSON.parse(localStorage.getItem('savedForms')) || [];
    let savedFormsContainer = document.getElementById('saved-forms');
    savedFormsContainer.innerHTML = ''; // Clear the saved forms

    savedForms.forEach((form, index) => {
        let formDiv = document.createElement('div');
        formDiv.className = 'saved-form';
        formDiv.innerHTML = 'Saved Form ' + (index + 1)
        formDiv.id = `saved-form ${index}`
        formDiv.onclick = function () {
            restoreForm(form);
        };
        savedFormsContainer.appendChild(formDiv);
    });
}

function restoreForm(formData) {
    let edgeContainer = document.getElementById('edge-container');
    edgeContainer.innerHTML = ''; // Clear existing inputs

    // Restore form values
    Object.keys(formData).forEach(key => {
        formData[key].forEach((value, index) => {
            let newInput = document.createElement('input');
            newInput.type = 'text';
            newInput.name = key;
            newInput.placeholder = 'start,end,weight';
            newInput.value = value;
            edgeContainer.appendChild(newInput);

            let br1 = document.createElement('br');
            let br2 = document.createElement('br');
            edgeContainer.appendChild(br1);
            edgeContainer.appendChild(br2);
        });
    });

    document.getElementById('edge-count').value = formData.edges.length;
}

function clearAll() {
    localStorage.removeItem('savedForms');
    loadSavedForms();
}