function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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

(function () {
    var map_el = document.getElementById('mapid');
    var rental_stories_el = document.getElementById('rental-stories');

    if (map_el) {
        var map = L.map('mapid').setView([46.2, 15], 8);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        const iconOptions = {
            iconSize  : [24, 30],
            iconAnchor: [12, 15],
            className : 'mymarker',
            popupAnchor: [0, -15],
        }

        if (rental_stories_el) {
            var stories = JSON.parse(rental_stories_el.innerText);

            stories.forEach((story) => {
                if (story.fields.lat && story.fields.lng && story.fields.icon) {

                    iconOptions.html = story.fields.icon;

                    const markerOptions = {
                        icon: L.divIcon(iconOptions)
                    };

                    L.marker([story.fields.lat, story.fields.lng], markerOptions)
                    .addTo(map)
                    .bindPopup(`
                    <div><p>${story.fields.description}</p></div>
                    <div class="d-flex justify-content-between">
                        <span>${story.fields.displayed_name}</span>
                        <span>PREBERI VEČ</span>
                    </div>
                `);
                }

            });
        } else {
            console.log('no rental stories');
        }
    } else {
        console.log('no map');
    }

})();

(function () {
    const chosen_emoji = document.getElementById('chosen-emoji');
    if (chosen_emoji) {
        document.querySelector('emoji-picker').addEventListener('emoji-click', event => {
            console.log(event.detail)
            chosen_emoji.innerHTML = event.detail.unicode;
            document.getElementById('id_icon').value = event.detail.unicode;
            chosen_emoji.click();
        });
    }
})();


(function () {
    const csrftoken = getCookie('csrftoken');

    const counter = {}
    $(".btn-clap").each(function() {
        counter[$(this).val()] = {
            debounce: null,
            clickCounter: 0
        }
    })

    $(".btn-clap").click(function(e) {
        e.stopPropagation();
        e.preventDefault();

        const id = $(this).val();
        const claps_no = parseInt($(this).children()[1].innerText);

        counter[id].clickCounter++;
        $(this).children()[1].innerText = claps_no + 1;

        clearTimeout(counter[id].debounce);

        // Update and log the counts after 3 seconds
        counter[id].debounce = setTimeout(function () {
            fetch(window.location.origin + "/clap/" + id, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
                },
                mode: 'same-origin',
                body: JSON.stringify({
                    claps_no: counter[id].clickCounter,
                }),
            })
            .then((res) => {
                if (res.ok) {
                    return res.text();
                }
                throw new Error("Response not ok");
            })
            counter[id].clickCounter = 0;
        }, 1000);
    });
})();

(function () {
    $(".read-more").each(function() {
        $(this).on('click', () => {
            const full_text = $(this).parent().parent().find('.story-description p:first-child');
            const shorter = $(this).parent().parent().find('.story-description p:last-child');

            if (shorter.css("display") === "none") {
                shorter.css("display", "inline");
                $(this).text = "PREBERI VEĆ";
                $(this).find("img").css("transform", "rotate(0)");
                full_text.css("display", "none");
            } else {
                shorter.css("display", "none");
                $(this).text = "PREBERI MANJ";
                $(this).find("img").css("transform", "rotate(180deg)");
                full_text.css("display", "inline");
            }
        })
    })
})();

function filterCategory() {
    console.log("filter")
    document.getElementById("search-header").value = '';
    document.getElementById("query-form").submit();
}


$(window).on('load', function() {
    const story_form_message = document.getElementById('modal-story-message');
    if (story_form_message) {
        $('#newStoryFormModal').modal('show');
    }
});
