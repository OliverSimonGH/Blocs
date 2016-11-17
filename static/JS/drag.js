//Allow elements to be dropped and do not(preven) go back to default

function allowDrop(ev) {
    ev.preventDefault();
}
// Drag feature that will transfer the  data and allow it to be draggable
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}
//Drop feautre (feature = code) that prevents the default and establishes the variable named "data" - which gets data and appends the child element
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}
