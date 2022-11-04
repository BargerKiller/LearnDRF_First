const loginForm = document.getElementById('login-form')
const baseEndpoint = 'http://localhost:8000'
const container = document.getElementById('container')
const searchForm = document.getElementById('search-form')
if (searchForm)
{
    searchForm.addEventListener('submit', (ev) =>
    {
        ev.preventDefault()
        let formData = new FormData(searchForm)
        let data = Object.fromEntries(formData)

        const endpoint = `${baseEndpoint}/search/?q=${data.search}`
        const options = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        }
        fetch(endpoint, options)
            .then(response =>
            {
                return response.json()
            })
            .then(writeToContainer)
            .catch(
                err =>
                {
                    console.log(err)
                }
            )
    })
}
if (loginForm)
{
    loginForm.addEventListener('submit', (ev) =>
    {
        ev.preventDefault()
        const loginEndpoint = `${baseEndpoint}/token/`
        let loginFormData = new FormData(loginForm)
        let loginObjectData = Object.fromEntries(loginFormData)
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify(loginObjectData),
        }
        fetch(loginEndpoint, options)
            .then(response =>
            {
                return response.json()
            })
            .then(authData =>
            {
                handleAuthData(authData, getProductList)
            })
            .catch(
                err =>
                {
                    console.log(err)
                }
            )
    })
}

function handleAuthData(authData, func)
{
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    func()
}

function writeToContainer(data)
{
    if (container)
    {
        container.innerHTML = `<pre>${JSON.stringify(data, null, 4)}</pre>`
    }
}

function getProductList()
{
    const endpoint = `${baseEndpoint}/products/`
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        }
    }
    fetch(endpoint, options)
        .then(response => response.json())
        .then(writeToContainer)
}
