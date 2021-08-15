(function () {
    var newsletterElems = document.querySelectorAll(".newsletter");
    newsletterElems.forEach(function (newsletterElem) {
        var form = newsletterElem.querySelector("form");
        var emailElem = form.querySelector("#email-newsletter");
        var submitButton = form.querySelector("button[type='submit']");
        var checkbox = form.querySelector("#confirm-email");
        var response = form.querySelector("#response");
        form.addEventListener("submit", (event) => {
            event.preventDefault();
            if (checkbox.checked) {
                form.classList.remove("error");
                submitButton.setAttribute("disabled", "disabled");
                emailElem.setAttribute("disabled", "disabled");
                checkbox.setAttribute("disabled", "disabled");
                fetch("https://podpri.djnd.si/api/subscribe/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        email: emailElem.value,
                        segment: 20,
                    }),
                })
                    .then((res) => {
                        if (res.ok) {
                            return res.text();
                        }
                        throw new Error("Response not ok");
                    })
                    .then((res) => {
                        response.className = "form-text text-start";
                        response.textContent = "Hvala za prijavo!";
                    })
                    .catch((error) => {
                        response.className = "form-text text-start text-error";
                        response.textContent = "Napaka pri prijavi :(";
                    })
                    .then(() => {
                        submitButton.removeAttribute("disabled");
                        emailElem.removeAttribute("disabled");
                        checkbox.removeAttribute("disabled");
                    });
            } else {
                form.classList.add("error");
            }
        });
    });
})();

(function () {
    var shareLinks = document.querySelectorAll(".social");
    shareLinks.forEach((shareLink) => {
        shareLink.addEventListener("click", function (event) {
            event.preventDefault();
            if (event.currentTarget.className.indexOf('isfbbox') !== -1) {
                const url = `https://www.facebook.com/dialog/feed?app_id=220548529891725&redirect_uri=${encodeURIComponent(document.location.href)}&link=${encodeURIComponent(document.location.href)}&ref=responsive`;
                window.open(url, '_blank');
            }
            if (event.currentTarget.className.indexOf('istwbox') !== -1) {
                const url = `https://twitter.com/intent/tweet?text=${encodeURIComponent(`${window.SHARE_TWEET_TEXT} ${document.location.href}`)}`;
                window.open(url, '_blank');
            }
            if (event.currentTarget.className.indexOf('isembox') !== -1) {
                const url = `mailto:?subject=NAJEMNIŠKI+SOS&body=${encodeURIComponent(window.SHARE_EMAIL_TEXT)}`;
                window.open(url, '_blank');
            }
        });
    });
})();
