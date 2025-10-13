// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', function () {
    // Create and add menu toggle button for mobile
    const headerContainer = document.querySelector('.header-container');
    const nav = document.querySelector('.nav');

    if (headerContainer && nav) {
        const menuToggle = document.createElement('button');
        menuToggle.classList.add('menu-toggle');
        menuToggle.innerHTML = '☰';
        menuToggle.setAttribute('aria-label', 'Toggle menu');

        headerContainer.appendChild(menuToggle);

        menuToggle.addEventListener('click', function () {
            nav.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', function (event) {
            if (!headerContainer.contains(event.target)) {
                nav.classList.remove('active');
            }
        });
    }

    // Handle responsive form layouts
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, select, button');
        inputs.forEach(input => {
            // Add responsive classes based on screen size
            window.addEventListener('resize', function () {
                if (window.innerWidth < 768) {
                    input.classList.add('mobile-full-width');
                } else {
                    input.classList.remove('mobile-full-width');
                }
            });

            // Trigger on load
            if (window.innerWidth < 768) {
                input.classList.add('mobile-full-width');
            }
        });
    });

    // Handle responsive grid adjustments
    function adjustGridLayout() {
        const appGrid = document.querySelector('.app-grid');
        if (appGrid) {
            const containers = appGrid.querySelectorAll('.container1, .container2');

            if (window.innerWidth < 768) {
                containers.forEach(container => {
                    container.style.marginBottom = '20px';
                });
            } else {
                containers.forEach(container => {
                    container.style.marginBottom = '';
                });
            }
        }
    }

    // Call on load and resize
    adjustGridLayout();
    window.addEventListener('resize', adjustGridLayout);

    // Handle responsive images
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.style.maxWidth = '100%';
        img.style.height = 'auto';
    });
});