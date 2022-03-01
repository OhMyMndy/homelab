
var page = 1;
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

var sid = urlParams.get('sid')
if (!sid) {
	sid = document.cookie
  .split('; ')
  .find(row => row.startsWith('ttrss_sid='))
  .split('=')[1];
}

var api_url = urlParams.get('url')
if (!api_url) {
	api_url = window.location.origin + "/api/"
}

function scrollRight() {
    page++;
    window.scrollTo(((window.innerWidth) * (page - 1)), 0)
}

function scrollLeft() {
    if (page > 1) {
        page--;
    }

    window.scrollTo(((window.innerWidth) * (page - 1)), 0)
}

document.onkeydown = checkKey;
function checkKey(e) {
    if (e.keyCode == 37) {
        scrollLeft();
        e.preventDefault();
    } else if (e.keyCode == 39) {
        scrollRight();
        e.preventDefault();
    }
}


function resize() {
    var height = window.innerHeight

    var elements = document.querySelectorAll(".newpaper-3")
    elements.forEach(function (element) {
        element.style["height"] = height + 'px'
        console.log(this)
    })
}


function data() {
    return {
        content: [],
        error: null,
        getHeadlines() {
            var data = {
                sid: sid,
                op: "getHeadlines",
                include_nested: true,
                feed_id: -4,
                limit: 10,
                unread_only: true,
                show_content: true,
                view_mode: "unread"
            }
            fetch(api_url, {
                method: 'POST',
                body: JSON.stringify(data),
            })
                .then((response) => response.json())
                .then(data => {
                    console.log(data)
                    try {
                        this.content = data.content
                        this.error = data.error
                        console.log(this.content)
                        console.log(this.error)
                    } catch (e) {
                        console.error(e)
                    }
                    resize()
                })

        },

        markAsRead(ids) {
            fetch(api_url, {
                method: "POST",
                body: JSON.stringify({ "ids": Array.of(ids), "sid": sid })
            })
                .then((response) => response.json())
                .then(data => this.content = data.content)
        },
        init() {
            try {
                this.getHeadlines()

            } catch (e) {
                console.error(e)
            }

        }
    }
}

