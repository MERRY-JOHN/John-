const loginsec = document.querySelector('.login-section');
const loginlink = document.querySelector('.login-link');
const registerlink = document.querySelector('.register-link');

[registerlink, loginlink].forEach(link => {
    link.addEventListener('click', () => {
        loginsec.classList.toggle('active');
    });
});