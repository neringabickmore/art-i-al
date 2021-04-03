// Remove item from the bag and reload the page on click
$('.remove-product').click(function (e) {
    let csrfToken = "{{ csrf_token }}";
    let itemId = $(this).attr('id').split('remove-')[1];
    let url = `/bag/remove/${itemId}/`;
    let data = {
        'csrfmiddlewaretoken': csrfToken,
    };

    fetch(url, data)
        .then(() => location.reload());
});