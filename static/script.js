document.addEventListener("DOMContentLoaded", function() {
    const images = [
        "{{ url_for('static', filename='images/hashiras.jpeg') }}",
        "{{ url_for('static', filename='images/muzan.png') }}",
        "{{ url_for('static', filename='images/gyutaro.png') }}"
    ];

    let currentIndex = 0;

    function changeBackground() {
        currentIndex = (currentIndex + 1) % images.length;
        document.body.style.backgroundImage = `url(${images[currentIndex]})`;
    }

    // Change image every 5 seconds (5000 milliseconds)
    setInterval(changeBackground, 5000);

    // Set initial background image
    document.body.style.backgroundImage = `url(${images[currentIndex]})`;
    document.body.style.backgroundImage = `url(${images[currentIndex]})`;
});
