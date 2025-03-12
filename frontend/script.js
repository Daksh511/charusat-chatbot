async function chat() {
    let query = document.getElementById("userQuery").value;

    let response = await fetch("https://charusat-chatbot-api-gcg9emg3emdkgbh3.southindia-01.azurewebsites.net/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
            , "Accept": "application/json"
        },
        body: JSON.stringify({ query: query }),
        mode: "cors" // Ensure CORS mode is enabled
    });

    let result = await response.json();
    document.getElementById("chatResponse").innerText = result.response;
}
