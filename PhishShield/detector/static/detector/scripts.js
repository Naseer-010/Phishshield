$(document).ready(function () {
    var dial = $(".dial .inner");
    var gauge_value = $(".gauge .value");

    function rotateDial() {
        var value = parseInt(gauge_value.text()); // Get value from HTML
        var deg = (value * 177.5) / 100; // Convert value to rotation degrees

        gauge_value.html(value + "%"); // Ensure value is displayed

        dial.css({ 'transform': 'rotate(' + deg + 'deg)' });
        dial.css({ '-ms-transform': 'rotate(' + deg + 'deg)' });
        dial.css({ '-moz-transform': 'rotate(' + deg + 'deg)' });
        dial.css({ '-o-transform': 'rotate(' + deg + 'deg)' });
        dial.css({ '-webkit-transform': 'rotate(' + deg + 'deg)' });
    }

    rotateDial(); // Run once on page load
});
