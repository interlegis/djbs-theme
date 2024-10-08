'use strict';
{
    window.addEventListener('load', function(e) {
        const toggler = document.querySelector("#sidenav-toggler");
        const target_selector = toggler.getAttribute("data-bs-target");
        function menuChanged() {
            localStorage.setItem("menuStatus", toggler.getAttribute("aria-expanded") == "true" ? "expanded" : "collapsed")
        }
        function setStatus(new_status) {
            const current_status = toggler.getAttribute("aria-expanded") == "true" ? "expanded" : "collapsed";
            if (current_status != new_status) {
                $(target_selector)
                if (new_status == "expanded") {
                    $(target_selector).collapse("show");
                } else {
                    $(target_selector).collapse("hide");
                }
                toggler.setAttribute("aria-expanded", new_status == "expanded");
            }
        }
        function initMenu() {
            const status = localStorage.getItem("menuStatus");
            status ? setStatus(status) : setStatus("expanded");
        }
        function setupMenu() {
            const target = document.querySelector(target_selector);
            target.addEventListener("hidden.bs.collapse", menuChanged);
            target.addEventListener("shown.bs.collapse", menuChanged);
            initMenu();
        }
        setupMenu();
    })
}
