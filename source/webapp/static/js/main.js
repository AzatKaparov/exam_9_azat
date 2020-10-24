async function addFavorite(event) {
    event.preventDefault();
    let likeBtn = event.target;
    let url = likeBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Добавлено в избранное")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Вы добавили фото в избранное.</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_success')
        setTimeout(() => note.remove(), 3000);
    }
    catch (error) {
        console.log(error);
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #721c24">Вы уже добававили это фото в избранное!</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_danger')
        setTimeout(() => note.remove(), 3000);
    }
}

async function removeFavorite(event) {
    event.preventDefault();
    let likeBtn = event.target;
    let url = likeBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Удалено из избранного")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Вы удалили фото из избранного</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_success')
        setTimeout(() => note.remove(), 3000);
    }
    catch (error) {
        console.log(error);
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #721c24">Вы уже удалили фото из избранного!</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_danger')
        setTimeout(() => note.remove(), 3000);
    }
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('add_fav');
    const removeButtons = document.getElementsByClassName('remove_fav');

    for (let btn of addButtons) {btn.onclick = addFavorite}
    for (let btn of removeButtons) {btn.onclick = removeFavorite}
});