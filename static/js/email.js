// defence for deleting email by accident
(function () {
    let message = "Do you really want to remove the selected e-mail address? If this is your only email it will not be removed.";
    let actions = document.getElementsByName('action_remove');
    if (actions.length) {
        actions[0].addEventListener("click", function (e) {
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    }
})();