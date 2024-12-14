document.addEventListener('DOMContentLoaded', function() {
    const link1 = document.getElementById('link1');
    const link2 = document.getElementById('link2');

    // Function to toggle the stylesheets
    function toggleStylesheet() {
        if (link1.disabled) {
            link1.disabled = false;
            link2.disabled = true;
        } else {
            link1.disabled = true;
            link2.disabled = false;
        }
    }

    // Event listener for clicks on the body
    document.body.addEventListener('click', toggleStylesheet);

    // Event listener for keyboard key presses
    document.addEventListener('keydown', function(event) {
        if (event.code === 'Enter' || event.code === 'Space') {
            toggleStylesheet();
        }
    });
});
