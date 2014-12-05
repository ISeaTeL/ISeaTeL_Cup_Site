$(function() {
    $('.open-popup-link').magnificPopup({
        // Class that is added to popup wrapper and background
        // make it unique to apply your CSS animations just to this exact popup
        removalDelay: 500,
        mainClass: 'mfp-fade',
        type: 'inline',
        midClick: true // Allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source in href.
    });
    $('.href-popup-link').magnificPopup({
        type: 'iframe',
        removalDelay: 500,
        mainClass: 'mmfp-fade',
        midClick: true,
        fixedContentPos: true
    });
})