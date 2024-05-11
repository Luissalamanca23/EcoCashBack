console.log("chatbot.js loaded");

require('dotenv').config();

const API_KEY = process.env.API_KEY;

async function getCompletion() {
    const res = await fetch('https://api.openai.com/v1/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Autorization': 'Bearer ' + APY_KEY
        },
        body: JSON.stringify({
            model: 'text-davinci-003',
            prompt: 'Once upon a time',
            max_tokens: 5,
            temperature: 0.5,
        })

    })

     const data = await res.json();
     consloe.log(data);
}

getCompletion();