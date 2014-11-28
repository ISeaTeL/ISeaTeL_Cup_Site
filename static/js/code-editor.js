var editor;
$(function() {
    editor = CodeMirror.fromTextArea(document.getElementById("code_editor"), {
        lineNumbers: true,
        styleActiveLine: true,
        matchBrackets: true,
        mode: "text/x-csrc",
        lineWrapping: true,
        tab: 4,
        indentUnit: 4,
        matchBrackets: true,
        theme: 'pastel-on-dark',
    });
    
    $('input[type=file]').bootstrapFileInput();
    $('.file-inputs').bootstrapFileInput();
    $('#fileinput').change(function(evt) {
        //Retrieve the first (and only!) File from the FileList object
        var f = evt.target.files[0];

        if (f) {
            var r = new FileReader();
            r.onload = function(e) {
                var contents = e.target.result;
                //alert("Got the file.\n" + "name: " + f.name + "\n" + "type: " + f.type + "\n" + "size: " + f.size + " bytes\n" + "starts with: " + contents.substr(1, contents.indexOf("\n")));
                editor.value = contents;
                try {
                    editor.getDoc().setValue(contents);
                } catch (e) {

                }
            }
            r.readAsText(f);
        } else {
            alert("Failed to load file");
        }
    })
})