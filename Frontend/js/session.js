const token =
localStorage.getItem("access_token");

if (!token) {
    window.location.href =
    "index.html";

}
const SESSION_TIME = 60 * 60 * 1000;

function startSessionTimer() {

    const loginTime =
    localStorage.getItem("login_time");

    if (!loginTime) return;

    setInterval(() => {

        const now = Date.now();

        const diff =
        now - parseInt(loginTime);

        if (diff >= SESSION_TIME) {

            const continuar = confirm(
                "Tu sesión expiró. ¿Deseas continuar?"
            );

            if (continuar) {

                localStorage.setItem(
                    "login_time",
                    Date.now()
                );

            }

            else {

                localStorage.clear();

                window.location.href =
                "index.html";

            }

        }

    }, 60000);

}

startSessionTimer();