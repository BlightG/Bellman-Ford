function addEdge() {
    let edgeContainer = document.getElementById('edge-container');
    let newInput = document.createElement('input');
    let newBreak = document.createElement('br')
    let newBreak2 = document.createElement('br')
    newInput.type = 'text';
    newInput.name = 'edges[]';
    newInput.placeholder = 'start,end,weight';
    edgeContainer.appendChild(newInput);
    edgeContainer.appendChild(newBreak);
    edgeContainer.appendChild(newBreak2);
}