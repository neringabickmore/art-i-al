// Notifies about the next image name
$('#new-img').change(function() {
    let file = $('#new-img')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});