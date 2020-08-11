var loadFile = function (event) {
    if (document.getElementById("output-label") !== null )
        document.getElementById("output-label").style.display = "none";
    document.getElementById("image-preview-holder").style.display = "block";

    var output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function () {
        URL.revokeObjectURL(output.src)
    }
};